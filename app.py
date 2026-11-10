
import streamlit as st

from langchain_config import get_news_articles

st.set_page_config(
    page_title="Equity Research News Tool",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Equity Research News Tool")
st.write("Search for the latest news articles about companies and industries.")

query = st.text_input("Enter company name or keyword")

if st.button("Get News"):

    if query.strip():

        try:
            with st.spinner("Fetching latest news..."):

                articles = get_news_articles(query.strip())

            if not articles:

                st.warning("No relevant news articles found.")

            else:

                st.subheader(f"Latest News for: {query}")

                for index, article in enumerate(articles, start=1):

                    with st.container(border=True):

                        left, right = st.columns([2, 1])

                        with left:

                            st.subheader(
                                f"{index}. {article.get('title', 'No title')}"
                            )

                            st.write(
                                article.get("description")
                                or "No description available."
                            )

                            source = article.get("source", {}).get(
                                "name", "Unknown"
                            )

                            published = article.get(
                                "publishedAt", "Unknown"
                            )

                            st.caption(
                                f"Source: {source} | Published: {published}"
                            )

                            url = article.get("url")

                            if url:
                                st.markdown(
                                    f"[Read Full Article]({url})"
                                )

                        with right:

                            image_url = article.get("urlToImage")

                            if image_url:
                                st.image(
                                    image_url,
                                    use_container_width=True
                                )
                            else:
                                st.info("Image not available")

        except Exception as e:

            st.error(f"An error occurred: {e}")

    else:

        st.warning("Please enter a company name or keyword.")
