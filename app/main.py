from contextlib import asynccontextmanager
from fastapi import FastAPI
from .utils.model_loader import load_all_models

models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.models = load_all_models()
    yield

app = FastAPI(title="Spam Detection API", version="1.0.0", lifespan=lifespan)

from .routes import email_detection
app.include_router(email_detection.router, prefix='/api')


