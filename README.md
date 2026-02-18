🚨 Emergency Call Center Traffic Prediction & Surge Detection using Machine Learning

Real-Time Emergency Traffic Forecasting & Anomaly Detection System
Built with Python • FastAPI • Streamlit • Scikit-Learn

📌 Project Overview

Emergency call centers manage high volumes of critical calls related to:

🚑 Medical Emergencies

🔥 Fire Incidents

👮 Police Assistance

🌪 Disaster & Severe Weather Events

Unexpected surges in call traffic can overload dispatch systems, delay emergency response, and increase operational risks.

This project builds an end-to-end Machine Learning system that:

✅ Predicts short-term emergency call traffic
✅ Detects abnormal surge patterns
✅ Simulates real-time monitoring
✅ Provides REST API for integration
✅ Supports proactive staffing & routing

🧠 Problem Statement

How can emergency systems:

Predict upcoming call volumes?

Detect abnormal spikes in real-time?

Allocate workforce proactively?

Prevent overload situations?

This system answers those questions using predictive modeling and anomaly detection.

🏗 System Architecture
Live Simulation / User Input
            ↓
     Streamlit Dashboard
            ↓
        FastAPI Backend
            ↓
  ML Regression Model + Isolation Forest
            ↓
Traffic Forecast + Surge Detection Alert

📁 Project Structure
emergency-call-ml/
│
├── data/
│   └── calls.csv
│
├── model/
│   └── model.pkl
│
├── backend/
│   └── api.py
│
├── frontend/
│   └── app.py
│
├── train.py
├── requirements.txt
└── README.md

📊 Dataset Description

Synthetic emergency call dataset simulating 30 days of activity with 5-minute intervals.

🔎 Features Used
Feature	Description
timestamp	Call received time
region	Geographic zone
call_type	Medical / Fire / Police / Other
call_duration	Duration in seconds
priority_level	Severity level
agent_available	Active agents
weather_flag	Normal / Severe
is_holiday	Holiday indicator
hour	Extracted time feature
day_of_week	Extracted time feature
is_weekend	Weekend flag
lag_1	Previous interval calls
rolling_call_count	Rolling 3-window count
moving_avg_3	Moving average
call_volume_next_interval	🎯 Target variable
🤖 Machine Learning Models
📈 Traffic Forecasting

Random Forest Regressor

Predicts next interval call volume

🚨 Surge Detection

Isolation Forest

Detects abnormal traffic spikes

📊 Model Performance

Mean Absolute Error (MAE): ~3.24

R² Score: ~0.80

This indicates strong predictive capability for short-term call volume forecasting.

⚙️ Technologies Used
Programming

Python

Core Libraries

Pandas

NumPy

Scikit-learn

FastAPI

Uvicorn

Streamlit

Requests

Deployment

Render (Cloud Web Service)

🚀 How to Run Locally
1️⃣ Clone Repository
git clone https://github.com/your-username/emergency-call-ml.git
cd emergency-call-ml

2️⃣ Create Virtual Environment
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Train Model (First Time Only)
python train.py


This generates:

model/model.pkl

5️⃣ Start Backend API
uvicorn backend.api:app --reload


Test:

http://127.0.0.1:8000

6️⃣ Start Frontend Dashboard

Open new terminal:

streamlit run frontend/app.py


Dashboard runs at:

http://localhost:8501

🌐 Deployment (Render)

Backend deployed using Render Web Service.

Build Command
pip install -r requirements.txt

Start Command
uvicorn backend.api:app --host 0.0.0.0 --port $PORT

🎯 Key Features

✔ End-to-End ML Pipeline
✔ Regression + Anomaly Detection
✔ Real-Time Traffic Simulation
✔ REST API Integration
✔ Clean Modular Structure
✔ Deployment Ready
✔ Production Thinking

💡 Real-World Use Cases

Smart City Emergency Monitoring

Disaster Response Optimization

Police & Medical Dispatch Planning

Emergency Workforce Forecasting

Public Safety Analytics

🔥 Future Improvements

XGBoost / Gradient Boosting Integration

LSTM Time-Series Forecasting

Kafka Real-Time Streaming

MLflow Experiment Tracking

Docker Containerization

CI/CD Pipeline

Multi-Region Scaling