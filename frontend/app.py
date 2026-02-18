import streamlit as st
import requests
import time
import random
import pandas as pd

# 🔥 Change this to your backend URL
BACKEND_URL = "https://emergency-call-prediction-1.onrender.com"

st.set_page_config(page_title="Emergency Call ML", layout="wide")

st.title("🚨 Emergency Call Traffic Monitoring System")

# ---------------------------------
# Mode Selection
# ---------------------------------

mode = st.sidebar.radio("Select Mode", ["Manual Prediction", "Live Simulation"])

# ---------------------------------
# Manual Prediction Mode
# ---------------------------------

if mode == "Manual Prediction":

    st.header("📌 Enter Call Details")

    region = st.selectbox("Region", ["North","South","East","West","Central"])
    call_type = st.selectbox("Call Type", ["Medical","Fire","Police","Other"])
    call_duration = st.slider("Call Duration", 100, 1200, 500)
    priority_level = st.slider("Priority Level", 1, 4, 2)
    agent_available = st.slider("Agents Available", 5, 30, 15)
    weather_flag = st.selectbox("Weather", ["Normal","Severe"])
    is_holiday = st.selectbox("Holiday", [0,1])
    hour = st.slider("Hour", 0, 23, 12)
    day_of_week = st.slider("Day of Week", 0, 6, 3)
    is_weekend = st.selectbox("Is Weekend", [0,1])
    lag_1 = st.slider("Previous Interval Calls", 0, 100, 20)
    rolling_call_count = st.slider("Rolling Call Count", 0, 200, 60)
    moving_avg_3 = st.slider("Moving Avg (3)", 0, 100, 25)

    if st.button("Predict"):

        data = {
            "region": region,
            "call_type": call_type,
            "call_duration": call_duration,
            "priority_level": priority_level,
            "agent_available": agent_available,
            "weather_flag": weather_flag,
            "is_holiday": is_holiday,
            "hour": hour,
            "day_of_week": day_of_week,
            "is_weekend": is_weekend,
            "lag_1": lag_1,
            "rolling_call_count": rolling_call_count,
            "moving_avg_3": moving_avg_3
        }

        try:
            response = requests.post(f"{BACKEND_URL}/predict", json=data)
            result = response.json()

            st.success(f"Predicted Call Volume: {result['predicted_call_volume']}")

            if result["surge_status"] == "SURGE DETECTED":
                st.error("🚨 SURGE DETECTED!")
            else:
                st.info("Normal Traffic")

        except:
            st.error("❌ Backend not reachable.")

# ---------------------------------
# Live Simulation Mode
# ---------------------------------

if mode == "Live Simulation":

    st.header("📊 Live Traffic Simulation")

    chart_data = pd.DataFrame({"Call Volume": []})
    chart = st.line_chart(chart_data)

    if st.button("Start Simulation"):

        for i in range(30):

            simulated_input = {
                "region": random.choice(["North","South","East","West","Central"]),
                "call_type": random.choice(["Medical","Fire","Police","Other"]),
                "call_duration": random.randint(100,1200),
                "priority_level": random.randint(1,4),
                "agent_available": random.randint(5,30),
                "weather_flag": random.choice(["Normal","Severe"]),
                "is_holiday": random.choice([0,1]),
                "hour": random.randint(0,23),
                "day_of_week": random.randint(0,6),
                "is_weekend": random.choice([0,1]),
                "lag_1": random.randint(10,60),
                "rolling_call_count": random.randint(30,150),
                "moving_avg_3": random.randint(15,60)
            }

            response = requests.post(f"{BACKEND_URL}/predict", json=simulated_input)
            result = response.json()

            new_data = pd.DataFrame({
                "Call Volume": [result["predicted_call_volume"]]
            })

            chart.add_rows(new_data)

            if result["surge_status"] == "SURGE DETECTED":
                st.error("🚨 SURGE DETECTED!")

            time.sleep(1)
