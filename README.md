# 🌉 FoodBridge AI

<div align="center">

<h3>Intelligent Surplus Food Redistribution System</h3>

<p>Connecting food donors with recipients using AI — reducing waste, feeding communities, saving the planet 🌍</p>

[![AI Powered](https://img.shields.io/badge/AI-Powered-brightgreen?style=for-the-badge)](https://github.com/shivasumedha/FoodBridge-AI-)
[![React](https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react)](https://github.com/shivasumedha/FoodBridge-AI-)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)](https://github.com/shivasumedha/FoodBridge-AI-)
[![SDG 2](https://img.shields.io/badge/SDG-2%20Zero%20Hunger-orange?style=for-the-badge)](https://sdgs.un.org/goals/goal2)
[![SDG 12](https://img.shields.io/badge/SDG-12%20Responsible%20Consumption-blue?style=for-the-badge)](https://sdgs.un.org/goals/goal12)
[![SDG 13](https://img.shields.io/badge/SDG-13%20Climate%20Action-green?style=for-the-badge)](https://sdgs.un.org/goals/goal13)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

</div>

---

## 📌 Table of Contents

- [About](#-about)
- [Problem Statement](#-problem-statement)
- [Solution](#-solution)
- [Screenshots](#-screenshots)
- [Features](#-features)
- [SDG Goals](#-sdg-goals)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [AI Features](#-ai-features)
- [Developer](#-developer)

---

## 🌟 About

FoodBridge AI is an intelligent food redistribution ecosystem developed as part of the 1M1B AI for Sustainability Virtual Internship in collaboration with IBM SkillsBuild and AICTE.

Every day, tons of edible food is wasted in hotels, hostels, restaurants, college canteens, and functions while orphanages, old-age homes, and shelters struggle to get enough food. FoodBridge AI creates a smart bridge between food donors and food receivers using Artificial Intelligence.

---

## ❗ Problem Statement

A significant amount of edible food is wasted daily due to poor coordination between food providers and organizations that require food. Most surplus food ends up in landfills, causing environmental pollution and resource wastage.

| Fact | Impact |
|------|--------|
| 🗑️ 40% of food is wasted globally | Massive resource loss |
| 😔 800 million people go hungry | Lives at risk daily |
| 🌍 8-10% of CO₂ from food waste | Climate crisis |

---

## 💡 Solution

- ✅ Donors register surplus food in seconds
- ✅ AI automatically finds the best nearby recipient
- ✅ Live map shows optimized delivery route
- ✅ Smart fallback ensures zero food goes to waste
- ✅ Real-time impact analytics dashboard

---

## 📸 Screenshots

### 🏠 Welcome Screen
![Welcome](screenshots/Screenshot_2026-06-16_131135.png)

### 🔐 Login and Role Selection
![Login](screenshots/Screenshot_2026-06-16_131201.png)

### 🏡 Main Dashboard
![Dashboard](screenshots/Screenshot_2026-06-16_131235.png)

### 🍱 Donor Register Surplus Food
![Donor](screenshots/Screenshot_2026-06-16_131416.png)

### 🗺️ AI Matching and Live Map
![AI Matching](screenshots/Screenshot_2026-06-16_131427.png)

### 📊 Impact Dashboard
![Impact](screenshots/Screenshot_2026-06-16_131438.png)

### 🎯 SDG Goals Progress
![SDG Goals](screenshots/Screenshot_2026-06-16_131515.png)

### 💬 Today's Good Wish
![Good Wish](screenshots/Screenshot_2026-06-16_131526.png)

### ⚙️ Backend API Running
![Backend](screenshots/Screenshot_2026-06-16_131537.png)

---

## ✨ Features

### For Donors
- Register surplus food with name, type, quantity, location
- AI powered food freshness check
- Real time donation status tracking
- Impact analytics — meals saved, CO₂ prevented

### For Recipients
- Browse available food donations nearby
- One click food acceptance
- Confetti celebration popup on acceptance
- Veg and Non-Veg compatibility filter

### AI Engine
- Smart recipient matching based on need and distance
- Food freshness prediction
- Live map with route optimization
- Demand forecasting from historical data
- Smart fallback system — Orphanage → Old-Age Home → Shelter → Goshala → Compost

### Dashboard
- Daily updates feed
- Weekly impact bar chart
- SDG goals progress tracker
- CO₂ emissions prevented counter
- Today's Good Wish section

---

## 🎯 SDG Goals

| SDG | Goal | How FoodBridge AI Helps |
|-----|------|------------------------|
| 🍽️ SDG 2 | Zero Hunger | Redirects surplus food to people in need |
| ♻️ SDG 12 | Responsible Consumption | Reduces food waste at source |
| 🌍 SDG 13 | Climate Action | Prevents CO₂ from food decomposition |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React, JavaScript, CSS3 |
| Backend | FastAPI, Python |
| Maps | Leaflet, OpenStreetMap |
| AI | IBM Granite Model, Custom Matching Engine |
| Version Control | Git, GitHub |

---

## 📁 Project Structure
FoodBridgeAI/

├── backend/

│   ├── main.py

│   ├── database.py

│   ├── models.py

│   ├── schemas.py

│   ├── routers/

│   │   ├── donors.py

│   │   ├── recipients.py

│   │   ├── food.py

│   │   └── ai_match.py

│   └── ai/

│       ├── freshness.py

│       ├── matching.py

│       └── fallback.py

├── frontend/

│   └── src/

│       ├── DonorDashboard.jsx

│       ├── RecipientDashboard.jsx

│       ├── ImpactDashboard.jsx

│       ├── ThankYouPopup.jsx

│       ├── DailyUpdatesFeed.jsx

│       └── useFoodData.js

└── screenshots/
git clone https://github.com/shivasumedha/FoodBridge-AI-.git

cd FoodBridge-AI-

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

cd backend

uvicorn main:app --reload
Runs at http://127.0.0.1:8000

### Frontend Setup
cd frontend

npm install

npm start
Runs at http://localhost:3000

---

## 🤖 AI Features

| Feature | Description |
|---------|-------------|
| 🧠 Smart Matching | Finds best recipient by need, distance and food type |
| 🌡️ Freshness Prediction | Estimates if food is safe for consumption |
| 🗺️ Route Optimization | Live map with fastest delivery route |
| 📈 Demand Forecasting | Predicts future food demand from history |
| ♻️ Fallback System | Ensures zero food goes to landfill |
| 📊 Impact Analytics | Tracks meals saved, CO₂ prevented, people fed |
---

## 👨‍💻 Developer

**Shiva Sumedha**

🎓 Internship — 1M1B AI for Sustainability Virtual Internship

🤝 In collaboration with IBM SkillsBuild and AICTE

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

🌱 Made with ❤️ to fight hunger and food waste

⭐ Star this repo if you found it helpful!

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=shivasumedha.FoodBridge-AI-)

</div>


