import requests
import os

API_KEY = os.getenv("GOOGLE_NEWS_API_KEY")
NEWS_URL = "https://newsapi.org/v2/everything"

def get_stock_news(ticker: str):
    params = {
        "q": ticker,
        "apiKey": API_KEY,
        "sortBy": "publishedAt",
        "language": "en",
    }
    response = requests.get(NEWS_URL, params=params)
    if response.status_code == 200:
        return response.json().get("articles", [])
    return []
