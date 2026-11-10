
from pathlib import Path

from openai import OpenAI
from newsapi import NewsApiClient
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


# Get project folder location
BASE_DIR = Path(__file__).parent


# Read API keys from text files
openai_api_key = (BASE_DIR / "API key.txt").read_text(
    encoding="utf-8"
).strip()

news_api_key = (BASE_DIR / "News API key.txt").read_text(
    encoding="utf-8"
).strip()


# Initialize OpenAI
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=openai_api_key,
    temperature=0
)


# Initialize NewsAPI
newsapi = NewsApiClient(api_key=news_api_key)


# Fetch news articles
def get_news_articles(query):

    articles = newsapi.get_everything(
        q=query,
        language="en",
        sort_by="relevancy",
        page_size=10
    )

    return articles["articles"]


# Extract article descriptions
def summarize_articles(articles):

    summaries = []

    for article in articles:
        description = article.get("description")

        if description:
            summaries.append(description)

    return " ".join(summaries)


# Get news summary text
def get_summary(query):

    articles = get_news_articles(query)

    summary = summarize_articles(articles)

    return summary


# Create prompt template
template = """
You are an AI assistant helping an equity research analyst.

Given the following query and the provided news article summaries,
provide an overall summary.

Query: {query}

Summaries: {summaries}

Provide a clear and relevant summary.
"""


prompt = PromptTemplate(
    template=template,
    input_variables=["query", "summaries"]
)


# Create LangChain chain
llm_chain = prompt | llm
