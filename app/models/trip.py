# from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, Enum, JSON
# from sqlalchemy.dialects.postgresql import UUID
# from sqlalchemy.sql import func
# from sqlalchemy.ext.declarative import declarative_base
# from uuid import uuid4

# Base = declarative_base()

# class Trip(Base):
#     __tablename__ = "trips"

#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
#     user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
#     place = Column(String, nullable=False)
#     budget = Column(Enum("Cheap", "Moderate", "Luxury", name="budget_levels"), nullable=False)
#     travel_type = Column(Enum("Solo", "Duo", "Family", "Friends", name="travel_types"), nullable=False)
#     duration = Column(Integer, nullable=False)
    
#     images = Column(JSON)  # List of image URLs
#     about = Column(Text)
#     top_activities = Column(JSON)  # List of activities
#     top_places = Column(JSON)  # List of must-visit places
#     itinerary = Column(JSON)  # AI-generated itinerary
#     local_cuisine = Column(JSON)  # Food recommendations
#     packing_checklist = Column(JSON)  # Suggested items to carry
#     best_time_to_visit = Column(String)
#     nearby_activities = Column(JSON)  # Other things to do nearby
    
#     created_at = Column(DateTime, default=func.now())
#     updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
