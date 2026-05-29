"""
Olympic sport endpoints.
Provides Olympic statistics and token consumption.
"""

from fastapi import APIRouter, HTTPException
from ..database import SessionLocal
from ..models import User
import csv

router = APIRouter()


@router.get("/sport/{sport_name}")
def get_sport(
    sport_name: str,
    user_id: int,
    country: str = None,
    year: int = None,
    medal: str = None
):
    """
    Retrieve Olympic medal statistics for a sport.

    Consumes one token from the user account and returns
    medal statistics based on the provided filters.
    """

    db = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")

    if user.tokens <= 0:
        db.close()
        raise HTTPException(status_code=400, detail="No tokens left")

    user.tokens -= 1
    tokens_left = user.tokens
    db.commit()

    db.close()

    results = []

    with open("app/data/olympics.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Sport"].lower() != sport_name.lower():
                continue

            if country and row["NOC"] != country:
                continue

            if year and int(row["Year"]) != year:
                continue

            if medal:
                if not row["Medal"]:
                    continue
                if row["Medal"].lower() != medal.lower():
                    continue

            results.append(row)

    gold = sum(1 for r in results if r["Medal"] == "Gold")
    silver = sum(1 for r in results if r["Medal"] == "Silver")
    bronze = sum(1 for r in results if r["Medal"] == "Bronze")

    return {
        "sport": sport_name,
        "results": {
            "gold": gold,
            "silver": silver,
            "bronze": bronze
        },
        "filters": {
            "country": country,
            "year": year,
            "medal": medal
        },
        "tokens_left": tokens_left
    }
