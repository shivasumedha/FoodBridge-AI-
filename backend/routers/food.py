from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/food", tags=["Food"])

@router.post("/", response_model=schemas.FoodDonationResponse)
def create_food_donation(food: schemas.FoodDonationCreate, db: Session = Depends(get_db)):
    db_food = models.FoodDonation(**food.dict())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

@router.get("/", response_model=list[schemas.FoodDonationResponse])
def get_all_food_donations(db: Session = Depends(get_db)):
    return db.query(models.FoodDonation).all()

@router.get("/{food_id}", response_model=schemas.FoodDonationResponse)
def get_food_donation(food_id: int, db: Session = Depends(get_db)):
    food = db.query(models.FoodDonation).filter(models.FoodDonation.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    return food

@router.put("/{food_id}/accept")
def accept_donation(food_id: int, recipient_id: int, db: Session = Depends(get_db)):
    food = db.query(models.FoodDonation).filter(models.FoodDonation.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    food.status = "accepted"
    food.matched_recipient_id = recipient_id
    db.commit()

    # Log impact
    impact = models.ImpactLog(
        donation_id=food.id,
        meals_saved=int(food.quantity * 4),
        people_fed=int(food.quantity * 3),
        food_waste_reduced_kg=food.quantity
    )
    db.add(impact)
    db.commit()
    return {"message": "Donation accepted successfully! ✅", "status": "accepted"}

@router.put("/{food_id}/decline")
def decline_donation(food_id: int, recipient_id: int, db: Session = Depends(get_db)):
    food = db.query(models.FoodDonation).filter(models.FoodDonation.id == food_id).first()
    if not food:
        raise HTTPException(status_code=404, detail="Food not found")
    food.status = "declined"
    db.commit()
    return {"message": "Donation declined", "status": "declined", "food_id": food_id}

@router.get("/pending/all")
def get_pending_donations(db: Session = Depends(get_db)):
    return db.query(models.FoodDonation).filter(
        models.FoodDonation.status.in_(["pending", "matched"])
    ).all()