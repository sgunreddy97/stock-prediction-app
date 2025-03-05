import firebase_admin
from firebase_admin import credentials, firestore
import os

# Firebase setup
cred = credentials.Certificate("firebase_credentials.json")  # Add your Firebase credentials
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_historical_data(ticker: str):
    """Fetch historical stock data from Firestore."""
    try:
        doc_ref = db.collection("stocks").document(ticker)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()["historical_data"]
        return None
    except Exception as e:
        print("Error fetching data:", e)
        return None
