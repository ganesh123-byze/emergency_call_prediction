# backend/api.py

from fastapi import FastAPI
import pickle
import pandas as pd
import uvicorn

app = FastAPI()

# Load model
with open("model/model.pkl", "rb") as f:
    model_data = pickle.load(f)

regressor = model_data["regressor"]
anomaly_model = model_data["anomaly_model"]
encoders = model_data["encoders"]
features = model_data["features"]


@app.get("/")
def home():
    return {"message": "Emergency Call Prediction API Running"}


@app.post("/predict")
def predict(data: dict):

    df = pd.DataFrame([data])

    # Encode categorical columns
    for col in ["region", "call_type", "weather_flag"]:
        df[col] = encoders[col].transform(df[col])

    prediction = regressor.predict(df[features])[0]

    anomaly_score = anomaly_model.predict(df[features])[0]

    surge_alert = "SURGE DETECTED" if anomaly_score == -1 else "Normal"

    return {
        "predicted_call_volume": int(prediction),
        "surge_status": surge_alert
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
