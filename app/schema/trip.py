# from pydantic import BaseModel, UUID4, Field
# from typing import List, Optional
# from datetime import datetime

# # Base Schema (Shared Fields)
# class TripBase(BaseModel):
#     place: str = Field(..., example="Paris")
#     budget: str = Field(..., example="Moderate")
#     travel_type: str = Field(..., example="Duo")
#     duration: int = Field(..., example=5)  # Number of days

#     images: Optional[List[str]] = Field(default=None, example=["https://example.com/image1.jpg"])
#     about: Optional[str] = Field(default=None, example="Paris is known for its art, fashion, and culture.")
#     top_activities: Optional[List[str]] = Field(default=None, example=["Eiffel Tower Visit", "Seine River Cruise"])
#     top_places: Optional[List[str]] = Field(default=None, example=["Louvre Museum", "Notre Dame Cathedral"])
#     itinerary: Optional[List[dict]] = Field(
#         default=None, 
#         example=[{"day": 1, "activities": ["Louvre visit", "Dinner at Seine"]}]
#     )
#     local_cuisine: Optional[List[str]] = Field(default=None, example=["Croissants", "Ratatouille"])
#     packing_checklist: Optional[List[str]] = Field(default=None, example=["Passport", "Sunglasses", "Camera"])
#     best_time_to_visit: Optional[str] = Field(default=None, example="Spring (March to May)")
#     nearby_activities: Optional[List[str]] = Field(default=None, example=["Wine Tasting", "Museum Hopping"])


# # Schema for Creating a Trip (Request)
# class TripCreate(TripBase):
#     pass  # All fields from TripBase are required for trip creation


# # Schema for Returning a Trip (Response)
# class TripResponse(TripBase):
#     id: UUID4
#     user_id: UUID4
#     created_at: datetime
#     updated_at: Optional[datetime] = None

#     class Config:
#         from_attributes = True  # Enables ORM support for SQLAlchemy
