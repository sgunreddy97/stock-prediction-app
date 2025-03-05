import pandas as pd
import numpy as np
from .database import get_historical_data

def moving_average(data, window=50):
    return data["close"].rolling(window=window).mean()

def calculate_macd(data):
    short_ema = data["close"].ewm(span=12, adjust=False).mean()
    long_ema = data["close"].ewm(span=26, adjust=False).mean()
    macd = short_ema - long_ema
    signal = macd.ewm(span=9, adjust=False).mean()
    return macd, signal

def rsi(data, period=14):
    delta = data["close"].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

def compute_technical_indicators(ticker: str):
    data = get_historical_data(ticker)
    if data is None:
        return None
    
    df = pd.DataFrame(data)
    df["50_day_MA"] = moving_average(df, 50)
    df["MACD"], df["Signal"] = calculate_macd(df)
    df["RSI"] = rsi(df)
    
    return df.to_dict(orient="records")
