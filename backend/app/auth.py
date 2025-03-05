import firebase_admin
from firebase_admin import auth

def create_user(email: str, password: str):
    """Create a new user in Firebase Auth."""
    try:
        user = auth.create_user(email=email, password=password)
        return {"uid": user.uid, "email": user.email}
    except Exception as e:
        return {"error": str(e)}

def verify_user(token: str):
    """Verify Firebase authentication token."""
    try:
        decoded_token = auth.verify_id_token(token)
        return {"uid": decoded_token["uid"], "email": decoded_token["email"]}
    except Exception as e:
        return {"error": str(e)}
