from pydantic import BaseModel
from typing import Optional

class DonorCreate(BaseModel):
    name: str
    email: str
    phone: str
    location: str

class DonorResponse(DonorCreate):
    id: int
    class Config:
        orm_mode = True

class RecipientCreate(BaseModel):
    name: str
    email: str
    phone: str
    location: str
    type: str
    food_preference: str
    capacity: int

class RecipientResponse(RecipientCreate):
    id: int
    class Config:
        orm_mode = True

class FoodDonationCreate(BaseModel):
    donor_id: int
    food_name: str
    food_type: str
    quantity: float
    unit: str
    prepared_time: str
    pickup_deadline: str
    location: str

class FoodDonationResponse(FoodDonationCreate):
    id: int
    status: str
    freshness_score: Optional[float]
    matched_recipient_id: Optional[int]
    class Config:
        orm_mode = True

class ImpactLogResponse(BaseModel):
    id: int
    donation_id: int
    meals_saved: int
    people_fed: int
    food_waste_reduced_kg: float
    class Config:
        orm_mode = True