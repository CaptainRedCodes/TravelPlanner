from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    username:str
    created_at: datetime

    class Config:
        orm_mode = True

class UserProfileUpdate(BaseModel):
    username:Optional[str]=None
    email:Optional[EmailStr]=None

class ChangePassword(BaseModel):
    old_password: str
    new_password: str