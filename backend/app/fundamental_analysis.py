import requests
import os

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
FUNDAMENTALS_URL = "https://www.alphavantage.co/query"

def get_fundamental_data(ticker: str):
    """Fetch company fundamentals from Alpha Vantage API."""
    params = {
        "function": "OVERVIEW",
        "symbol": ticker,
        "apikey": API_KEY,
    }
    response = requests.get(FUNDAMENTALS_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return {}
