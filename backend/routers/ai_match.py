from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from ai.freshness import calculate_freshness_score
from ai.matching import get_best_match
from ai.fallback import get_fallback_match
import models

router = APIRouter(prefix="/ai", tags=["AI Engine"])

@router.get("/freshness/{food_id}")
def check_freshness(food_id: int, db: Session = Depends(get_db)):
    food = db.query(models.FoodDonation).filter(models.FoodDonation.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    result = calculate_freshness_score(food.prepared_time, food.pickup_deadline)
    food.freshness_score = result["freshness_score"]
    db.commit()
    return result

@router.get("/match/{food_id}")
def match_recipient(food_id: int, db: Session = Depends(get_db)):
    food = db.query(models.FoodDonation).filter(models.FoodDonation.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    freshness = calculate_freshness_score(food.prepared_time, food.pickup_deadline)
    if not freshness["safe_for_donation"]:
        return {"matched": False, "reason": "Food is not safe ❌", "freshness": freshness}

    match = get_best_match(food, db)

    if match["matched"]:
        food.matched_recipient_id = match["recipient_id"]
        food.status = "matched"
        db.commit()
        return {"freshness": freshness, "match": match}
    else:
        fallback = get_fallback_match(food, db)
        if fallback["matched"]:
            food.matched_recipient_id = fallback["recipient_id"]
            food.status = "matched"
            db.commit()
        return {"freshness": freshness, "match": match, "fallback": fallback}

@router.get("/next-match/{food_id}")
def get_next_match(food_id: int, exclude_id: int, db: Session = Depends(get_db)):
    food = db.query(models.FoodDonation).filter(models.FoodDonation.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")

    fallback = get_fallback_match(food, db, exclude_id=exclude_id)
    if fallback["matched"]:
        food.matched_recipient_id = fallback["recipient_id"]
        food.status = "matched"
        db.commit()
    return fallback

@router.get("/impact")
def get_impact(db: Session = Depends(get_db)):
    donations = db.query(models.FoodDonation).filter(
        models.FoodDonation.status.in_(["accepted", "delivered"])
    ).all()
    total_food_kg = sum(d.quantity for d in donations if d.unit == "kg")
    meals_saved = int(total_food_kg * 4)
    people_fed = int(meals_saved * 0.8)
    return {
        "total_donations": len(donations),
        "total_food_kg": round(total_food_kg, 2),
        "meals_saved": meals_saved,
        "people_fed": people_fed,
        "co2_prevented_kg": round(total_food_kg * 2.5, 2)
    }