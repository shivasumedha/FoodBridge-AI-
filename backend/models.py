from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base

class Donor(Base):
    __tablename__ = "donors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    location = Column(String)
    created_at = Column(DateTime, default=func.now())

class Recipient(Base):
    __tablename__ = "recipients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String)
    location = Column(String)
    type = Column(String)  # orphanage, old-age home, shelter, NGO
    food_preference = Column(String)  # veg, non-veg, both
    capacity = Column(Integer)
    created_at = Column(DateTime, default=func.now())

class FoodDonation(Base):
    __tablename__ = "food_donations"
    id = Column(Integer, primary_key=True, index=True)
    donor_id = Column(Integer)
    food_name = Column(String)
    food_type = Column(String)  # veg or non-veg
    quantity = Column(Float)
    unit = Column(String)  # kg, plates, liters
    prepared_time = Column(String)
    pickup_deadline = Column(String)
    location = Column(String)
    status = Column(String, default="pending")  # pending, matched, delivered
    matched_recipient_id = Column(Integer, nullable=True)
    freshness_score = Column(Float, nullable=True)
    created_at = Column(DateTime, default=func.now())

class ImpactLog(Base):
    __tablename__ = "impact_logs"
    id = Column(Integer, primary_key=True, index=True)
    donation_id = Column(Integer)
    meals_saved = Column(Integer)
    people_fed = Column(Integer)
    food_waste_reduced_kg = Column(Float)
    created_at = Column(DateTime, default=func.now())