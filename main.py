# pintu masuk
from fastapi import FastAPI
from database import engine, Base
from routes import user, todo

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(todo.router)

@app.get("/")
def root():
    return {"message": "API is running"}