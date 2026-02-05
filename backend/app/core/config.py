import os
from pydantic import BaseModel

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:postgres@db:5432/postgres")

class Settings(BaseModel):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALG: str = "HS256"
    JWT_EXPIRES_MIN: int = 60

def get_settings() -> Settings:
    return Settings(
        DATABASE_URL=os.environ["DATABASE_URL"],
        JWT_SECRET=os.environ["JWT_SECRET"],
        JWT_ALG=os.getenv("JWT_ALG", "HS256"),
        JWT_EXPIRES_MIN=int(os.getenv("JWT_EXPIRES_MIN", "60")),
    )