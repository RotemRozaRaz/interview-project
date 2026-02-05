from fastapi import FastAPI
from backend.db import Base, engine
import backend.models as models


app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)