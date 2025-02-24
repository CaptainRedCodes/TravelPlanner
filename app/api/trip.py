from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.trip import Trip
from app.db.dependency import get_db
from app.schema.trip import TripCreate, TripResponse
from app.services.tripServices import generate_trip_data
from app.core.security import oauth2_scheme, verify_token

router = APIRouter()

@router.post("/generate/", status_code=201, response_model=TripResponse)
def create_trip(
    trip_data: TripCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """Generate and store trip details based on user input"""
    payload = verify_token(token)
    user_id = payload.get("user_id")
    
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate trip details
    trip_details = generate_trip_data(trip_data)

    new_trip = Trip(
        user_id=int(user_id),
        place=trip_data.place,
        budget=trip_data.budget,
        travel_type=trip_data.travel_type,
        duration=trip_data.duration,
        images=trip_details["images"],
        about=trip_details["about"],
        top_activities=trip_details["top_activities"],
        top_places=trip_details["top_places"],
        itinerary=trip_details["itinerary"],
        local_cuisine=trip_details["local_cuisine"],
        packing_checklist=trip_details["packing_checklist"],
        best_time_to_visit=trip_details["best_time_to_visit"],
        nearby_activities=trip_details["nearby_activities"]
    )
    
    try:
        db.add(new_trip)
        db.commit()
        db.refresh(new_trip)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
    
    return new_trip

@router.get("/get/{trip_id}", response_model=TripResponse)
def get_trip(trip_id: int, db: Session = Depends(get_db)):
    """Fetch trip details by ID"""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    return trip
