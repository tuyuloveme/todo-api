from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from database import get_db
from models.todo import TodoDB
from schemas.todo import TodoCreate, TodoResponse

router = APIRouter()

@router.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate, user_id: int, db: Session = Depends(get_db)):
    new_todo = TodoDB(
        title=todo.title,
        completed=todo.completed,
        user_id=user_id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.get("/todos", response_model=list[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    return db.query(TodoDB).options(joinedload(TodoDB.user)).all()