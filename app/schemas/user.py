from typing import Optional

from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None # Password can be optional for update

class UserInDBBase(UserBase):
    id: int

    class Config:
        from_attributes = True # For Pydantic v2, use from_attributes=True instead of orm_mode=True

class User(UserInDBBase):
    pass
