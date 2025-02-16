from pydantic import BaseModel, EmailStr
from datetime import datetime
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