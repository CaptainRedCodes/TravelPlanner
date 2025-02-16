from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema.user import UserCreate, UserProfileUpdate, ChangePassword
from app.core.security import get_current_user
from app.models.user import User
from app.db.dependency import get_db
from app.utils.hashing import hashed_password, verify_password

router = APIRouter()

@router.post("/register/")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(username=user.username, email=user.email, password=hashed_password(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/profile/")
def get_profile(current_user: User = Depends(get_current_user)):
    """Retrieve the currently logged-in user's profile."""
    return {
        "username": current_user.username,
        "email": current_user.email,
        "created_at": current_user.created_at
    }

@router.put("/profile/update/")
def update_profile(profile_data: UserProfileUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Update the user's profile details."""
    if profile_data.username:
        existing_user = db.query(User).filter(User.username == profile_data.username).first()
        if existing_user and existing_user.id != current_user.id:
            raise HTTPException(status_code=400, detail="Username already taken")
        current_user.username = profile_data.username

    if profile_data.email:
        existing_email = db.query(User).filter(User.email == profile_data.email).first()
        if existing_email and existing_email.id != current_user.id:
            raise HTTPException(status_code=400, detail="Email already taken")
        current_user.email = profile_data.email

    db.commit()
    db.refresh(current_user)
    return {"message": "Profile updated successfully"}

@router.put("/profile/change-password/")
def change_password(password_data: ChangePassword, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Allow users to change their password."""
    if not verify_password(password_data.old_password, current_user.password):
        raise HTTPException(status_code=400, detail="Old password is incorrect")

    current_user.password = hashed_password(password_data.new_password)
    db.commit()
    return {"message": "Password updated successfully"}
