
import streamlit as st

from langchain_config import llm_chain, get_summary, get_news_articles

st.set_page_config(
    page_title="Equity Research News Tool",
    page_icon="📰",
    layout="wide"
)

st.title("Equity Research News Tool")

st.write(
    "Enter your query to get the latest news articles summarized."
)

query = st.text_input("Query")

if st.button("Get News"):

    if query:

        try:
            with st.spinner("Fetching news articles..."):

                articles = get_news_articles(query)

            if not articles:

                st.warning("No relevant news articles found.")

            else:

                st.subheader("Latest News Articles")

                for index, article in enumerate(articles, start=1):

                    st.markdown(
                        f"### {index}. {article.get('title', 'No title')}"
                    )

                    st.write(
                        article.get("description")
                        or "No description available."
                    )

                    st.caption(
                        f"Source: {article.get('source', {}).get('name', 'Unknown')} "
                        f"| Published: {article.get('publishedAt', 'Unknown')}"
                    )

                    url = article.get("url")

                    if url:
                        st.markdown(f"[Read Full Article]({url})")

                    st.divider()

                st.subheader("AI Generated Summary")

                st.info(
                    "AI summarization is temporarily unavailable. "
                    "News articles are being fetched successfully."
                )

        except Exception as e:

            st.error(f"An error occurred: {e}")

    else:

        st.warning("Please enter your query.")
