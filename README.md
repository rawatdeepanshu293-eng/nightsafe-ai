# nightsafe-ai
AI-powered risk-aware navigation for safer night travel
# 🌙 NightSafe

NightSafe is an AI-powered, risk-aware navigation system designed to make cities safer after dark.  
It predicts potentially dangerous routes using historical crime patterns, road conditions (potholes), and real-time context to help users choose safer paths at night.

---

## 🚨 Problem Statement
At night, the shortest route is often not the safest one.  
Existing navigation systems optimize for speed, not safety, leaving pedestrians vulnerable in poorly lit or high-risk areas.

---

## 💡 Solution
NightSafe introduces **risk-aware navigation** by assigning a live risk score to city routes based on:
- Crime history patterns
- Road condition risks (potholes, poor lighting)
- Time-of-day and night-specific context
- User’s live location

Instead of just “fastest routes,” NightSafe recommends **safer alternatives**.

---

## ⚙️ Key Features
- Live location-based risk assessment
- AI-inspired risk scoring model
- Night-specific safety intelligence
- Risk-aware route recommendations
- City-level risk insights for planners

---

## 🧠 How It Works
1. User’s live location is detected
2. Multiple urban risk factors are analyzed
3. An AI model computes a **relative risk score**
4. Routes are classified as Low, Medium, or High risk
5. Safer navigation options are suggested

---

## 🏗️ Tech Stack
- **Python** – Risk prediction logic
- **Flask** – Backend API
- **JavaScript** – Frontend logic
- **HTML/CSS** – User interface
- **Open Data** – Crime and infrastructure datasets (simulated)

---

## 🌍 Sustainable Development Goal Alignment
**SDG 11 – Sustainable Cities and Communities**

NightSafe supports:
- Safer and more inclusive urban mobility
- Data-driven smart city planning
- Night-time safety for pedestrians and vulnerable groups

---

## ▶️ How to Run the Project

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.p
