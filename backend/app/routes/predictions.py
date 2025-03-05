from fastapi import APIRouter
from ..models import predict_stock_price

router = APIRouter()

@router.get("/{ticker}/predict")
def predict_stock(ticker: str, days: int = 30):
    return {"ticker": ticker, "predictions": predict_stock_price(ticker, days)}
