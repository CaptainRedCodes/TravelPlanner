from app.models.user import Base as UserBase
from app.models.trip import Base as TripBase
from app.db.session import engine

# Create all tables
UserBase.metadata.create_all(bind=engine)
