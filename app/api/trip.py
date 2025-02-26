from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.trip import Trip
from app.db.dependency import get_db
from app.schema.trip import TripCreate, TripResponse, TripUpdate
from app.services.tripServices import generate_trip_data
from app.core.security import oauth2_scheme, verify_token
from typing import List

router = APIRouter()

@router.post("/generate/", status_code=201, response_model=TripResponse)
def create_trip(
    trip_data: TripCreate,
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """Generate and store trip details for multiple destinations"""
    payload = verify_token(token)
    user_id = payload.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Generate AI-powered trip details
    trip_details = generate_trip_data(trip_data)

    new_trip = Trip(
        user_id=int(user_id),
        places=trip_data.places,  # Now supports multiple places
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
def get_trip(trip_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """Fetch trip details by ID"""

    payload = verify_token(token)
    user_id = payload.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    trip = db.query(Trip).filter(Trip.id == trip_id).first()

    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    if trip.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not Authorized to access this trip")

    return trip

    
@router.put("/update-trip/{trip_id}")
def update_trip(trip_id: int, trip_update: TripUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """Update an existing trip."""
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    
    payload = verify_token(token)
    user_id = payload.get("user_id")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == int(user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")

    if trip.user_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this trip")

    # Update only provided fields
    update_data = trip_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(trip, key, value)

    # Generate AI-enhanced trip details based on new data
    ai_generated_data = generate_trip_data(trip)

    # Update AI-generated fields in DB
    for key, value in ai_generated_data.items():
        setattr(trip, key, value)

    db.commit()
    db.refresh(trip)

    return {"message": "Trip updated successfully", "updated_trip": trip}
