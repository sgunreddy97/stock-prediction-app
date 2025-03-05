from fastapi import APIRouter
from ..technical_analysis import compute_technical_indicators
from ..fundamental_analysis import get_fundamental_data

router = APIRouter()

@router.get("/{ticker}/technical")
def get_technical_data(ticker: str):
    return compute_technical_indicators(ticker)

@router.get("/{ticker}/fundamentals")
def get_fundamental_info(ticker: str):
    return get_fundamental_data(ticker)
