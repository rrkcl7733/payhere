from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    password: str


class UserInDBBase(UserBase):
    id: int
    password: Optional[str] = None

    class Config:
        orm_mode = True


class UserRead(UserInDBBase):
    pass