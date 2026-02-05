from fastapi import APIRouter, Depends
from backend.app.api.deps import get_current_user
from backend.app.schemas.user import UserOut
from backend.app.models.user import User

router = APIRouter(tags=["users"])

@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    return current_user
