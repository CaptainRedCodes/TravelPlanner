# app/models/trip.py
from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.base import Base
from app.schema.trip import BudgetLevel, TravelType  # Import the Enums

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    place = Column(String(255), nullable=False)
    budget = Column(Enum(BudgetLevel), nullable=False)
    travel_type = Column(Enum(TravelType), nullable=False)
    duration = Column(Integer, nullable=False)
    
    # JSON fields for lists
    images = Column(JSON, default=list)
    about = Column(Text)
    top_activities = Column(JSON, default=list)
    top_places = Column(JSON, default=list)
    itinerary = Column(JSON, default=list)
    local_cuisine = Column(JSON, default=list)
    packing_checklist = Column(JSON, default=list)
    best_time_to_visit = Column(String(100))
    nearby_activities = Column(JSON, default=list)
    
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    user = relationship("User", back_populates="trips")
