from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserOut(BaseModel):
    id: int
    email: EmailStr
    display_name: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True
