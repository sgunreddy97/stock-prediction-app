from fastapi import APIRouter, HTTPException
from ..auth import create_user

router = APIRouter()

@router.post("/register")
def register_user(email: str, password: str):
    result = create_user(email, password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
