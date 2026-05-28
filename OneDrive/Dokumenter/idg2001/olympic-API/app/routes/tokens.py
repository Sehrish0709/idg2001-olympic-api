from fastapi import APIRouter
import httpx
from ..database import SessionLocal
from ..models import User

router = APIRouter()


@router.post("/tokens/")
def add_tokens(user_id: int, amount: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    user.tokens += amount

    db.commit()
    db.refresh(user)
    db.close()

    return {"tokens": user.tokens}


@router.post("/tokens/redeem")
def redeem_tokens(user_id: int, code: str):
    db = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        db.close()
        return {"error": "User not found"}

    response = httpx.post(
        "http://token-shop:8001/validate",
        json={"code": code}
    )

    data = response.json()

    if "error" in data:
        db.close()
        return data

    user.tokens += data["tokens"]

    db.commit()
    db.refresh(user)
    db.close()

    return {
        "message": "Tokens added",
        "tokens": user.tokens
    }