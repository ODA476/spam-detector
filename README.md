# AI Spam Detector API

A machine learning microservice built with **FastAPI** and **Scikit-Learn** to classify messages as Spam or Ham.

## 🚀 Quick Start
1. **Install dependencies**: `pip install -r requirements.txt`
2. **Run locally**: `uvicorn app.main:app --reload`
3. **Open API Docs**: Navigate to `http://127.0.0.1:8000/docs`

## 🐳 Docker Deployment
```bash
docker build -t spam-detector .
docker run -p 80:80 spam-detector