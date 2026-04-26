from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base 

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    todos = relationship("TodoDB", back_populates="user")
    