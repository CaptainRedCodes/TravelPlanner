from sqlalchemy import Column, Integer, String
from app.db.session import engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), nullable=False,unique=True)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String)

# Create tables if they don’t exist
Base.metadata.create_all(bind=engine)
