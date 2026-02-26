# 🚨 Emergency Call Volume Prediction & Surge Detection System

A production-ready Machine Learning web application that predicts emergency call volume and detects surge patterns in real-time.

🌐 **Live Demo:**  
https://emergency-call-prediction-2.onrender.com/

---

## 📌 Project Overview

This project predicts emergency call traffic and identifies potential surge situations using machine learning.

It is designed to simulate real-world emergency response systems where accurate forecasting helps authorities allocate resources efficiently.

---

## 🚀 Features

- 📊 Emergency Call Volume Prediction
- 📈 Live Traffic Simulation
- ⚠ Surge Detection Logic
- 🌐 Deployed Cloud Application (Render)
- 🔄 Automated CI Pipeline (GitHub Actions)
- 📦 Model Serialization using Pickle
- 🧪 Automated Model Validation in CI

---

## 🏗 Project Architecture


Emergency_call_prediction/
│
├── backend/
│ ├── api.py
│
├── frontend/
│ ├── app.py
│
├── model/
│ └── model.pkl
│
├── train.py
├── requirements.txt
├── Dockerfile
└── .github/workflows/ci.yml


---

## ⚙️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Flask / FastAPI (if applicable)
- GitHub Actions (CI)
- Render (Cloud Deployment)
- Docker

---

## 🔄 CI/CD Pipeline

This project uses **GitHub Actions** for Continuous Integration.

### Pipeline performs:

- Dependency installation
- Model loading validation
- Unit test execution
- Build verification on every push to `main`

If any step fails, deployment is stopped.

---

## 🧠 Machine Learning Workflow

1. Data preprocessing
2. Feature engineering
3. Model training
4. Performance evaluation
5. Model serialization (`model.pkl`)
6. Deployment
7. Automated CI validation

---

## 🧪 Model Validation in CI

The CI pipeline verifies that:

- `model.pkl` exists
- Model loads successfully
- Dependencies install correctly

This ensures production stability.

---

## 📦 Installation (Local Setup)

Clone the repository:


git clone https://github.com/ganesh123-byze/emergency_call_prediction.git

cd emergency_call_prediction


Create virtual environment:


python -m venv venv
venv\Scripts\activate (Windows)


Install dependencies:


pip install -r requirements.txt


Run application:


python backend/api.py


or (if Streamlit):


streamlit run frontend/app.py


---

## ☁ Deployment

The application is deployed on **Render**.

Deployment is automatically triggered after successful CI checks.

---

## 🎯 Future Improvements

- Model performance threshold validation in CI
- Real-time monitoring & logging
- Automatic model retraining pipeline
- REST API documentation (Swagger)
- Performance benchmarking

---

## 👨‍💻 Author

Ganesh Pedagada  
Aspiring Cloud & Machine Learning Engineer  

---

## ⭐ If You Like This Project

Give it a star ⭐ on GitHub!

