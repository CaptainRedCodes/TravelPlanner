from pydantic import BaseModel,field_validator,Field
from enum import Enum
from typing import Optional, List
from datetime import datetime

# Enum for budget levels
class BudgetLevel(str, Enum):
    Cheap = "Cheap"
    Moderate = "Moderate"
    Luxury = "Luxury"

# Enum for travel type
class TravelType(str, Enum):
    Solo = "Solo"
    Duo = "Duo"
    Family = "Family"
    Friends = "Friends"

# Schema for user input (Trip creation)
class TripCreate(BaseModel):
    place: str
    budget: BudgetLevel
    travel_type: TravelType
    duration: int



# Schema for API response (Full trip details)
class TripResponse(TripCreate):
    id: int
    images: Optional[List[str]] = Field(default_factory=list)
    about: Optional[str] = None
    top_activities: Optional[List[str]] = Field(default_factory=list)
    top_places: Optional[List[str]] = Field(default_factory=list)
    itinerary: Optional[List[str]] = Field(default_factory=list)
    local_cuisine: Optional[List[str]] = Field(default_factory=list)
    packing_checklist: Optional[List[str]] = Field(default_factory=list)
    best_time_to_visit: Optional[str] = None
    nearby_activities: Optional[List[str]] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Correct usage for SQLAlchemy model conversion
