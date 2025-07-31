from fastapi import FastAPI
from app.core.database import SessionLocal
from app.api.v1 import user_routes

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
