from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.core.security import create_access_token, authenticate_user, oauth2_scheme
from app.db.dependency import get_db
from app.core.verification import verify_token
# Define the router
router = APIRouter()

@router.post("/token",status_code=200)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    if user.is_verified==False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Please Verify your email before Login!")
    
    access_token = create_access_token(
        data={"sub": user.username}, 
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/verify-token/")
def verify_user_token(token: str = Depends(oauth2_scheme)):
    """Verify JWT token validity."""
    return {"message": "Token is valid"}

@router.get("/verify-email/{token}")
def verify_email(token: str, db: Session = Depends(get_db)):
    
    try:
        user = verify_token(token, db)
        return {"message": f"Email {user.email} verified successfully!"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
