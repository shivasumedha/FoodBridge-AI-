from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import donors, recipients, food, ai_match

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FoodBridge AI",
    description="Intelligent Surplus Food Redistribution System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(donors.router)
app.include_router(recipients.router)
app.include_router(food.router)
app.include_router(ai_match.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to FoodBridge AI 🌱",
        "status": "running"
    }