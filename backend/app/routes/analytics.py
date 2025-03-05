from fastapi import APIRouter
from ..sentiment_analysis import analyze_sentiment

router = APIRouter()

@router.get("/{ticker}/sentiment")
def get_sentiment_analysis(ticker: str):
    return analyze_sentiment(ticker)
