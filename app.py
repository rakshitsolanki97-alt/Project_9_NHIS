
import streamlit as st

from langchain_config import (
    get_news_articles,
    get_news_summary,
    get_article_image
)

st.set_page_config(page_title="Equity Research News Tool", page_icon="📰", layout="wide")

st.title("📰 Equity Research News Tool")

st.write("Search for the latest company and industry news " "with AI-powered analysis.")

query = st.text_input("Enter Company Name Or Keyword", placeholder="Example: Samsung, Tesla, Apple")

if st.button("Get News", type="primary"):

    if not query.strip():

        st.warning("Please enter a company name or keyword.")

    else:

        try:

            with st.spinner("Fetching latest news..."): articles = get_news_articles(query.strip())

            if not articles: st.warning("No relevant news articles found.")

            else:

                st.success(f"{len(articles)} news articles found for {query}.")

                st.subheader("🤖 AI News Summary")

                try:

                    with st.spinner("Gemini is analyzing the news..."):
                        summary = get_news_summary(query, articles)

                    st.markdown(summary)

                except Exception as error:

                    st.warning(
                        "AI summary is temporarily unavailable. "
                        "You can still read all the news articles below."
                    )

                    st.error(f"Gemini Error Details: {error}")

                st.divider()

                st.subheader(f"📰 Latest News for: {query}")

                for index, article in enumerate(articles, start=1):

                    with st.container(border=True):

                        left, right = st.columns([2.3, 1])

                        with left:

                            st.subheader(f"{index}. {article.get('title') or 'No title'}")

                            st.write(article.get("description") or "No description available.")

                            source = article.get("source", {}).get("name", "Unknown")

                            published = article.get("publishedAt", "Unknown")

                            st.caption(f"Source: {source} | Published: {published}")

                            article_url = article.get("url")

                            if article_url:
                                st.markdown(f"[Read Full Article]({article_url})")

                        with right:

                            try:

                                image_data = get_article_image(article)

                                if image_data: st.image(image_data["url"],width=260)

                            except Exception:
                                pass

        except Exception as error:

            st.error(f"Application Error: {error}")
