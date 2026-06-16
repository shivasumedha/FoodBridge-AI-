from sqlalchemy.orm import Session
import models

RECIPIENT_PRIORITY = ["orphanage", "old-age home", "shelter", "NGO"]

def get_best_match(food: models.FoodDonation, db: Session) -> dict:
    recipients = db.query(models.Recipient).all()

    if not recipients:
        return {"matched": False, "reason": "No recipients registered"}

    compatible = []
    for r in recipients:
        if r.food_preference == "both":
            compatible.append(r)
        elif r.food_preference == food.food_type:
            compatible.append(r)

    if not compatible:
        return {"matched": False, "reason": "No compatible recipients found"}

    # Sort by priority
    def priority_score(recipient):
        rtype = recipient.type.lower()
        for i, p in enumerate(RECIPIENT_PRIORITY):
            if p in rtype:
                return i
        return len(RECIPIENT_PRIORITY)

    compatible.sort(key=priority_score)
    best = compatible[0]

    return {
        "matched": True,
        "recipient_id": best.id,
        "recipient_name": best.name,
        "recipient_type": best.type,
        "recipient_location": best.location,
        "food_preference": best.food_preference
    }