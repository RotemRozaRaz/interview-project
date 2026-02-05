from fastapi import FastAPI
from backend.app.api.routes.auth import router as auth_router
from backend.app.api.routes.users import router as users_router
from backend.app.db import base  # noqa: F401


app = FastAPI()


app.include_router(auth_router)
app.include_router(users_router)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}
