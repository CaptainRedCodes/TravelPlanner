from pydantic import BaseModel, EmailStr, field_validator
from datetime import datetime
from typing import Optional
import re

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    is_verified: bool=False


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    
class UserOut(BaseModel):
    id: int
    email: EmailStr
    username:str
    created_at: datetime
    is_verified:bool

    @field_validator("is_verified")
    @classmethod
    def check_verification(cls, value):
        """Raise an error if the user is not verified"""
        if not value:
            raise ValueError("User account is not verified. Please verify your email.")
        return value

    """Uncomment it during final"""
    # @validator("password")
    # def validate_password(cls, value):
    #     """Enforce strong password policy"""
    #     if len(value) < 8:
    #         raise ValueError("Password must be at least 8 characters long")
    #     if not re.search(r"[A-Z]", value):
    #         raise ValueError("Password must contain at least one uppercase letter (A-Z)")
    #     if not re.search(r"[a-z]", value):
    #         raise ValueError("Password must contain at least one lowercase letter (a-z)")
    #     if not re.search(r"\d", value):
    #         raise ValueError("Password must contain at least one digit (0-9)")
    #     if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
    #         raise ValueError("Password must contain at least one special character (!@#$%^&* etc.)")
    #     username = values.get("username","").lower()
    #     if username and username in value.lower():
    #         raise ValueError("Password cannot be Username")

    #     return value
    class Config:
        from_attributes = True

class UserProfileUpdateWithPassword(BaseModel):
    email:Optional[EmailStr]=None
    old_password: str
    new_password: str

    @field_validator("new_password", mode="before")
    def validate_password(cls, new_password, values):
        if values.get("old_password") and not new_password:
            raise ValueError("New password is required when changing password.")
        return new_password
    