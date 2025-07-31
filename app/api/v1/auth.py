from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.user import User
from app.api.deps import get_db
from app.schemas.auth import UserLogin

router = APIRouter()


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):

    username = data.username
    password = data.password

    user = db.query(User).filter_by(username=username).first()

    if not user:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail={
            "username": "User not found by this username"
        })

    return {
        "username": username,
        "password": password
    }
