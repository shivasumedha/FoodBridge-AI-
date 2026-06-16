from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/recipients", tags=["Recipients"])

@router.post("/", response_model=schemas.RecipientResponse)
def create_recipient(recipient: schemas.RecipientCreate, db: Session = Depends(get_db)):
    existing = db.query(models.Recipient).filter(models.Recipient.email == recipient.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_recipient = models.Recipient(**recipient.dict())
    db.add(db_recipient)
    db.commit()
    db.refresh(db_recipient)
    return db_recipient

@router.get("/", response_model=list[schemas.RecipientResponse])
def get_all_recipients(db: Session = Depends(get_db)):
    return db.query(models.Recipient).all()

@router.get("/{recipient_id}", response_model=schemas.RecipientResponse)
def get_recipient(recipient_id: int, db: Session = Depends(get_db)):
    recipient = db.query(models.Recipient).filter(models.Recipient.id == recipient_id).first()
    if not recipient:
        raise HTTPException(status_code=404, detail="Recipient not found")
    return recipient