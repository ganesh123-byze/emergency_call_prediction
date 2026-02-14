# train.py

import pandas as pd
import numpy as np
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score

# ------------------------------
# 1. Load Dataset
# ------------------------------

df = pd.read_csv("data/calls.csv")

# ------------------------------
# 2. Feature Selection
# ------------------------------

features = [
    "region",
    "call_type",
    "call_duration",
    "priority_level",
    "agent_available",
    "weather_flag",
    "is_holiday",
    "hour",
    "day_of_week",
    "is_weekend",
    "lag_1",
    "rolling_call_count",
    "moving_avg_3"
]

target = "call_volume_next_interval"

# ------------------------------
# 3. Encoding Categorical Features
# ------------------------------

encoders = {}

for col in ["region", "call_type", "weather_flag"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# ------------------------------
# 4. Train Test Split
# ------------------------------

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------
# 5. Train Regression Model
# ------------------------------

regressor = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# ------------------------------
# 6. Train Surge Detection Model
# ------------------------------

anomaly_model = IsolationForest(
    contamination=0.05,
    random_state=42
)

anomaly_model.fit(X)

# ------------------------------
# 7. Save Model
# ------------------------------

os.makedirs("model", exist_ok=True)

model_data = {
    "regressor": regressor,
    "anomaly_model": anomaly_model,
    "encoders": encoders,
    "features": features
}

with open("model/model.pkl", "wb") as f:
    pickle.dump(model_data, f)

print("✅ Model saved successfully!")
