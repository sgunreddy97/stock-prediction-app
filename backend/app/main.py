from fastapi import FastAPI
from .routes import users, stocks, predictions, analytics

app = FastAPI(title="Stock Prediction API")

# Include all API routes
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(stocks.router, prefix="/stocks", tags=["Stocks"])
app.include_router(predictions.router, prefix="/predictions", tags=["Predictions"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])

@app.get("/")
def root():
    return {"message": "Stock Prediction API is running!"}
