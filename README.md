
# Project 9 – Equity Research News Tool

## 1. Project Overview

The Equity Research News Tool is an AI-powered news research application that fetches the latest business and company-related news articles and provides AI-generated summaries.

The application uses NewsAPI to retrieve relevant news articles, Google Gemini to analyze and summarize the news, and Streamlit to provide a simple and interactive user interface.

## 2. Project Objectives

- Fetch the latest news related to companies and industries.
- Display relevant news articles with titles, descriptions, and images.
- Use Google Gemini AI to analyze and summarize news articles.
- Provide important business updates and developments.
- Identify positive and negative business impacts.
- Present the results through a user-friendly web application.

## 3. Technologies Used

- Python
- Streamlit
- NewsAPI
- LangChain
- Google Gemini AI
- Python Dotenv
- Requests
- BeautifulSoup

## 4. Features

### News Retrieval
Fetches relevant English-language news articles using NewsAPI.

### AI-Powered News Summary
Uses Google Gemini AI through LangChain to analyze news articles and generate concise summaries.

### Article Images
Displays available article images. If an original image is unavailable, the application attempts to find an image from the article webpage or Wikimedia Commons.

### Interactive Interface
Provides a Streamlit interface where users can search for companies and keywords.

### Error Handling
Displays appropriate error messages when news retrieval or AI summarization fails.

## 5. Project Structure

```text
Project 9/
│
├── app.py
├── langchain_config.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
├── Project 9.pptx
│
└── venv/
```

## 6. Installation and Setup

### Step 1: Clone the Repository

Download or clone the project repository to your computer.

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

## 7. API Configuration

The application requires API keys for NewsAPI and Google Gemini AI.

Create a file named `.env` in the project root directory.

Add your own API keys in the following format:

```env
NEWS_API_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder values with your own valid API keys.

**Important:** API keys are confidential. Never upload the `.env` file to GitHub or share your API keys publicly.

## 8. Running the Application

After completing the installation and API configuration, run:

```bash
streamlit run app.py
```

The application will open in your default web browser.

Enter a company name or keyword in the search box and click the **Get News** button.

The application will retrieve relevant news articles and attempt to generate an AI-powered summary.

## 9. Testing and Validation

The application can be tested using company names and business-related keywords such as:

- Tata Motors
- Tesla
- Apple
- Samsung

Testing includes:

- Checking news retrieval.
- Verifying article titles and descriptions.
- Checking image availability.
- Testing Gemini AI summarization.
- Validating error handling.

AI summarization availability depends on the Gemini API service, account limits, and network connectivity.

## 10. Future Enhancements

- Export news summaries to PDF.
- Save previous searches.
- Add company-wise news analysis.
- Improve news filtering and categorization.
- Add historical news analysis.
- Improve the user interface.

## 11. Conclusion

The Equity Research News Tool combines news retrieval and Large Language Model technology to simplify business news research.

It helps users collect relevant company news, understand important developments, and obtain concise AI-generated insights through an interactive web application.