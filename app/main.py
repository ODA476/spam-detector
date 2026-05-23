from contextlib import asynccontextmanager
from fastapi import FastAPI
from .utils.model_loader import load_all_models

models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load all models once at startup
    global models
    models = load_all_models()
    yield
    # Optional: cleanup if needed (close connections, etc.)
    models.clear()

app = FastAPI(title="Spam Detection API", version="1.0.0")

from .routes import email_detection
app.include_router(email_detection.router, prefix='/api')


