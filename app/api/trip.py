# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app.models.trip import Trip
# from app.db.dependency import get_db
# from app.schema.trip import TripCreate, TripResponse
# from app.services.tripServices import generate_trip_data

# @router.post("/generate", response_model=TripResponse)
# def create_trip(trip_data: TripCreate, db: Session = Depends(get_db)):
#     """Generate trip details based on user input"""
#     generated_data = generate_trip_data(trip_data)
#     new_trip = Trip(**trip_data.dict(), **generated_data)
#     db.add(new_trip)
#     db.commit()
#     db.refresh(new_trip)
#     return new_trip

# @router.get("/{trip_id}", response_model=TripResponse)
# def get_trip(trip_id: str, db: Session = Depends(get_db)):
#     """Fetch trip details by ID"""
#     trip = db.query(Trip).filter(Trip.id == trip_id).first()
#     if not trip:
#         raise HTTPException(status_code=404, detail="Trip not found")
#     return trip