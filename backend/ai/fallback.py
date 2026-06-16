from sqlalchemy.orm import Session
import models

FALLBACK_PRIORITY = [
    "orphanage",
    "old-age home",
    "shelter",
    "NGO",
    "animal farm",
    "goshala",
    "compost",
    "biogas"
]

def get_fallback_match(food: models.FoodDonation, db: Session, exclude_id: int = None) -> dict:
    recipients = db.query(models.Recipient).all()

    for priority in FALLBACK_PRIORITY:
        for r in recipients:
            if exclude_id and r.id == exclude_id:
                continue
            if priority in r.type.lower():
                if r.food_preference == "both" or r.food_preference == food.food_type:
                    return {
                        "matched": True,
                        "fallback": True,
                        "priority_level": FALLBACK_PRIORITY.index(priority) + 1,
                        "recipient_id": r.id,
                        "recipient_name": r.name,
                        "recipient_type": r.type,
                        "recipient_location": r.location
                    }

    return {
        "matched": False,
        "fallback": True,
        "reason": "No fallback recipient available — send to compost"
    }