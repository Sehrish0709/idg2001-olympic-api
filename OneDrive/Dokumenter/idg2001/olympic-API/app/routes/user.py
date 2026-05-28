from fastapi import APIRouter
from ..database import SessionLocal
from ..models import User

router = APIRouter()


@router.post("/user/")
def create_user(email: str, password: str):
    db = SessionLocal()
    user = User(email=email.strip(), password=password, tokens=100)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user


@router.get("/user/")
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users


@router.get("/user/{user_id}")
def get_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user


@router.delete("/user/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    db.close()
    return {"message": "User deleted"}


@router.put("/user/{user_id}")
def update_user(user_id: int, email: str = None, password: str = None):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()

    if email:
        user.email = email.strip()
    if password:
        user.password = password

    db.commit()
    db.refresh(user)
    db.close()

    return user