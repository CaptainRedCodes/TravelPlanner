import hashlib
import uuid
from sqlalchemy.orm import Session
from app.models .user import User
from app.services.emailServices import send_verification_email

def generate_verification_token(email: str, db: Session):
    """Generate a hashed UUID token and store it in DB."""
    raw_token = str(uuid.uuid4()) 
    hashed_token = hashlib.sha256(raw_token.encode()).hexdigest()
    
    user = db.query(User).filter(User.email == email).first()
    if user:
        user.verification_token = hashed_token
        db.commit()
    return raw_token  

def verify_token(token: str, db: Session):
    """Validate UUID token against hashed value in database."""
    hashed_token = hashlib.sha256(token.encode()).hexdigest()
    user = db.query(User).filter(User.verification_token == hashed_token).first()
    
    if not user:
        raise ValueError("Invalid token")
    
    user.is_verified = True
    user.verification_token = None  
    db.commit()
    return user
