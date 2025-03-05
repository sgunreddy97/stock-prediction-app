from textblob import TextBlob
from .news_scraper import get_stock_news

def analyze_sentiment(ticker: str):
    """Analyze sentiment of stock-related news articles."""
    articles = get_stock_news(ticker)
    sentiments = []
    
    for article in articles:
        text = article["title"] + " " + article["description"]
        sentiment_score = TextBlob(text).sentiment.polarity
        sentiments.append(sentiment_score)

    if sentiments:
        avg_sentiment = sum(sentiments) / len(sentiments)
        return {"ticker": ticker, "sentiment_score": avg_sentiment}
    
    return {"ticker": ticker, "sentiment_score": 0}
