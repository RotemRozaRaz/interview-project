from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt

from backend.app.core.config import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, password_hash: str) -> bool:
    return pwd_context.verify(password, password_hash)

def create_access_token(subject: str) -> str:
    now = datetime.now(timezone.utc)
    exp = now + timedelta(minutes=settings.JWT_EXPIRES_MIN)
    payload = {"sub": subject, "iat": int(now.timestamp()), "exp": exp}

    token = jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALG)

    # ✅ compatibility: PyJWT<2 returns bytes, PyJWT>=2 returns str
    if isinstance(token, bytes):
        token = token.decode("utf-8")

    return token

def decode_token(token: str) -> dict:
    # jwt.PyJWT יזרוק חריגות אם פג תוקף/לא תקין
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALG])
