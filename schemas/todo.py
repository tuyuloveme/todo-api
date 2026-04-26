from pydantic import BaseModel
from schemas.user import UserResponse

class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
    user: UserResponse

    class Config:
        from_attribute = True