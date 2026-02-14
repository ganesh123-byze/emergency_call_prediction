import streamlit as st
import requests
import time
import random
import pandas as pd

st.title("🚨 Emergency Call Traffic Monitoring System")

st.header("Live Traffic Simulation")

chart_data = pd.DataFrame({"Call Volume": []})
chart = st.line_chart(chart_data)

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

    response = requests.post("http://127.0.0.1:8000/predict", json=simulated_input)
    result = response.json()

    new_data = pd.DataFrame({"Call Volume": [result["predicted_call_volume"]]})
    chart.add_rows(new_data)

    if result["surge_status"] == "SURGE DETECTED":
        st.error("🚨 SURGE DETECTED!")
    else:
        st.success("Normal Traffic")

    time.sleep(1)
