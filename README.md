
# News Research Tool

## Project Overview
The News Research Tool is a Python-based web application that fetches the latest news articles based on a user-provided search query.

The application uses NewsAPI to retrieve relevant news articles and Streamlit to provide a simple and interactive user interface.

## Features
- Search news articles using a keyword or company name.
- Fetch the latest relevant news articles.
- Display article titles and descriptions.
- Display news source and publication date.
- Provide links to read full articles.
- AI summarization integration using LangChain and OpenAI.

## Technologies Used
- Python
- Streamlit
- LangChain
- OpenAI
- NewsAPI

## Project Structure
Project 9/
- app.py
- langchain_config.py
- requirements.txt
- README.md
- API key.txt
- News API key.txt

## Installation

1. Clone or download the project.
2. Open the project folder in VS Code.
3. Create and activate a virtual environment.
4. Install dependencies:

   pip install -r requirements.txt

5. Add your API keys in the respective text files:
   - API key.txt
   - News API key.txt

## Run the Application

Execute the following command in the terminal:

streamlit run app.py

## Current Status
News article fetching and display functionality has been tested successfully.

AI summarization is integrated into the project configuration but is temporarily unavailable because OpenAI API credits are not enabled.

## Conclusion
This project demonstrates how Python, NewsAPI, Streamlit, and LangChain can be used to build a news research application.
