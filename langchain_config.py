
import os
import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from newsapi import NewsApiClient

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


# Load API keys
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


# Fetch relevant news articles
def get_news_articles(query):

    if not NEWS_API_KEY:
        raise ValueError("NEWS_API_KEY is missing in .env file.")

    newsapi = NewsApiClient(api_key=NEWS_API_KEY)

    response = newsapi.get_everything(q=query, language="en", sort_by="relevancy", page_size=10)

    return response.get("articles", [])


# Gemini AI prompt
prompt = PromptTemplate(
    input_variables=["query", "articles"],
    template="""
You are a professional equity research assistant.

Analyze these news articles about {query}.

Provide:
1. Important news updates.
2. Major business developments.
3. Positive and negative impacts.
4. Overall conclusion.

Use simple and clear English.
Keep the summary concise.

News Articles:
{articles}
""")


# Connect to Gemini
def get_gemini_model():

    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is missing in .env file.")

    return ChatGoogleGenerativeAI(model="gemini-3.8-flash", google_api_key=GEMINI_API_KEY, temperature=0, max_output_tokens=500, timeout=60, max_retries=1)


# Generate AI summary using 3 articles
def get_news_summary(query, articles):

    if not articles:
        return "No news articles found."

    article_text = ""

    for index, article in enumerate(articles[:3], start=1):

        title = article.get("title") or "No title"
        description = article.get("description") or "No description"

        article_text += (f"\nArticle {index}: {title}\n"f"{description[:250]}\n")

    chain = prompt | get_gemini_model()

    response = chain.invoke({"query": query, "articles": article_text})

    return response.content


# Check whether an image URL works
def is_valid_image(image_url):

    if not image_url:
        return False

    try:

        response = requests.get(image_url, headers={"User-Agent": "Mozilla/5.0"}, stream=True, timeout=8)

        content_type = response.headers.get("Content-Type", "")

        valid = (response.status_code == 200 and content_type.startswith("image/"))

        response.close()

        return valid

    except requests.RequestException:
        return False


# Get image from article webpage
def get_webpage_image(article_url):

    try:

        response = requests.get(article_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=8)

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        image = soup.find("meta", property="og:image")

        if not image:
            image = soup.find("meta", attrs={"name": "twitter:image"})

        if image:

            image_url = image.get("content")

            if is_valid_image(image_url):
                return image_url

    except requests.RequestException:
        pass

    return None

# Calculate image title relevance
def image_relevance(article_title, image_title):

    stop_words = {"the", "and", "for", "with", "from", "this", "that", "have", "will", "says", "said", "about", "after", "before", "their", "they",
                "into", "over", "under", "what", "when", "where", "why", "how", "new", "latest"}

    article_words = set(re.findall(r"[a-z0-9]+", article_title.lower())) - stop_words

    image_words = set(re.findall(r"[a-z0-9]+", image_title.lower())) - stop_words

    return len(article_words.intersection(image_words))


# Search relevant images on Wikimedia Commons
def search_related_image(article):

    title = article.get("title") or ""

    if not title:
        return None

    try:

        response = requests.get(
            "https://commons.wikimedia.org/w/api.php",
            params={"action": "query", "format": "json", "generator": "search", "gsrsearch": title[:120], "gsrnamespace": 6,
                    "gsrlimit": 5, "prop": "imageinfo", "iiprop": "url", "iiurlwidth": 800},
            headers={"User-Agent": "Project9NewsResearchTool/1.0"}, timeout=10)

        response.raise_for_status()

        data = response.json()

        pages = data.get("query", {}).get("pages", {})

        candidates = []

        for page in pages.values():

            image_title = page.get("title", "")

            score = image_relevance(title, image_title)

            if score < 1:
                continue

            image_info = page.get("imageinfo", [])

            if not image_info:
                continue

            image_url = (image_info[0].get("thumburl") or image_info[0].get("url"))

            if image_url: candidates.append((score, image_url))

        candidates.sort(key=lambda item: item[0], reverse=True)

        for score, image_url in candidates:

            if is_valid_image(image_url):
                return image_url

    except (requests.RequestException, ValueError, KeyError):
        return None

    return None


# Get best available article image
def get_article_image(article):

    original_image = article.get("urlToImage")

    if is_valid_image(original_image):
        return {"url": original_image}

    article_url = article.get("url")

    if article_url:

        webpage_image = get_webpage_image(article_url)

        if webpage_image:
            return {"url": webpage_image}

    related_image = search_related_image(article)

    if related_image:
        return {"url": related_image}

    return None
