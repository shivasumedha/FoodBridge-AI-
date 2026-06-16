from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/donors", tags=["Donors"])

@router.post("/", response_model=schemas.DonorResponse)
def create_donor(donor: schemas.DonorCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Donor).filter(models.Donor.email == donor.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_donor = models.Donor(**donor.dict())
    db.add(db_donor)
    db.commit()
    db.refresh(db_donor)
    return db_donor

@router.get("/", response_model=list[schemas.DonorResponse])
def get_all_donors(db: Session = Depends(get_db)):
    return db.query(models.Donor).all()

@router.get("/{donor_id}", response_model=schemas.DonorResponse)
def get_donor(donor_id: int, db: Session = Depends(get_db)):
    donor = db.query(models.Donor).filter(models.Donor.id == donor_id).first()
    if not donor:
        raise HTTPException(status_code=404, detail="Donor not found")
    return donor