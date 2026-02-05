from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from backend.app.db.session import SessionLocal
from backend.app.core.security import decode_token
from backend.app.models.user import User


# -------------------------
# DB dependency
# -------------------------
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -------------------------
# Auth dependencies
# -------------------------
bearer_scheme = HTTPBearer(auto_error=True)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    """
    Extracts Bearer token, validates JWT,
    fetches current user from DB.

    Raises:
    - 401 if token is invalid / expired
    - 401 if user does not exist
    """
    token = credentials.credentials

    try:
        payload = decode_token(token)
        user_id = payload.get("sub")
        if user_id is None:
            raise ValueError("Token missing subject")
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    user = db.get(User, int(user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user
