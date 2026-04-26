from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models.user import UserDB
from schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/user", response_model=UserResponse)
def create_user( user: UserCreate, db: Session = Depends(get_db)):
    new_user = UserDB(name=user.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user