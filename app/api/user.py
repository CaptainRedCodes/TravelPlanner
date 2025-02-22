from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schema.user import UserCreate, UserProfileUpdateWithPassword
from app.core.security import get_current_user
from app.models.user import User
from app.db.dependency import get_db
from app.utils.hashing import hashed_password, verify_password
from app.core.verification import generate_verification_token
from app.services.emailServices import send_verification_email
router = APIRouter()

@router.post("/register/",status_code=200)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user_name = db.query(User).filter(User.username == user.username).first()
    db_user_email = db.query(User).filter(User.email == user.email).first()
    
    if db_user_name or db_user_email:
        raise HTTPException(status_code=400, detail="User with simi lar credentials already exists")


    new_user = User(username=user.username, email=user.email, password=hashed_password(user.password),is_verified=False,)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    raw_token = generate_verification_token(user.email, db)

    # Send verification email
    await send_verification_email(user.email, raw_token)

   
    return {"message":"Awaiting for Confirmation"}

@router.get("/profile/")
def get_profile(current_user: User = Depends(get_current_user)):
    """Retrieve the currently logged-in user's profile."""
    return {
        "username": current_user.username,
        "email": current_user.email,
        "created_at": current_user.created_at
    }

@router.put("/profile/update/")
def update_profile(
    profile_data: UserProfileUpdateWithPassword, 
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    
    if profile_data.email:
        existing_email = db.query(User).filter(User.email == profile_data.email).first()
        if existing_email and existing_email.id != current_user.id:
            raise HTTPException(status_code=400, detail="Email already in use")
        current_user.email = profile_data.email

    if profile_data.old_password and profile_data.new_password:
        if not verify_password(profile_data.old_password, current_user.password):
            raise HTTPException(status_code=400, detail="Old password is incorrect")
        current_user.password = hashed_password(profile_data.new_password)

    db.commit()
    db.refresh(current_user)
    return {"message": "Profile updated successfully"}

