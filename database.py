import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# koneksi ke postgresql
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

# session buat komunikasi ke database
SessionLocal = sessionmaker(bind=engine)

# base untuk model
Base = declarative_base()

# dependency buat dipakai di routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()