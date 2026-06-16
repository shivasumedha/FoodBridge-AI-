# 🌉 FoodBridge AI

<div align="center">

![FoodBridge AI](screenshots/Screenshot%202026-06-16%20131235.png)

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

**FoodBridge AI** is an intelligent food redistribution ecosystem developed as part of the **1M1B AI for Sustainability Virtual Internship** in collaboration with **IBM SkillsBuild & AICTE**.

Every day, tons of edible food is wasted in hotels, hostels, restaurants, college canteens, and functions — while orphanages, old-age homes, and shelters struggle to get enough food. FoodBridge AI creates a smart bridge between food donors and food receivers using Artificial Intelligence.

---

## ❗ Problem Statement

> A significant amount of edible food is wasted daily
Orphanage → Old-Age Home → Shelter → Goshala → Compost
### 📊 Dashboard
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
| Database | SQLite / PostgreSQL |
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

---

## ⚙️ Installation

### Backend Setup
```bash
git clone https://github.com/shivasumedha/FoodBridge-AI-.git
cd FoodBridge-AI-
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
cd backend
uvicorn main:app --reload
```
> Runs at http://127.0.0.1:8000

### Frontend Setup
```bash
cd frontend
npm install
npm start
```
> Runs at http://localhost:3000

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

🎓 **Internship:** 1M1B AI for Sustainability Virtual Internship

🤝 **In collaboration with:** IBM SkillsBuild & AICTE

---

## 📄 License

This project is licensed under the MIT License.

---

<div align="center">

🌱 Made with ❤️ to fight hunger and food waste

⭐ Star this repo if you found it helpful!

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=shivasumedha.FoodBridge-AI-)

</div>


