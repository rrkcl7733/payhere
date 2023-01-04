from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: EmailStr


class UserCreate(UserBase):
    password: str