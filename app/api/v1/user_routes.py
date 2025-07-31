from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..deps import get_db

from app.crud import user_crud
from app.schemas.user import UserSchema, UserCrudSchema

router = APIRouter()


@router.post("/create/", response_model=UserSchema)
def create_user(user_data: UserCrudSchema, db: Session = Depends(get_db)):
    return user_crud.create(db, obj_in=user_data)


@router.get("/list/", response_model=List[UserSchema])
def read_users(skip: Optional[int] = None, limit: Optional[int] = None, db: Session = Depends(get_db)):
    return user_crud.list(db, skip=skip, limit=limit)



@router.get("/detail/{pk}", response_model=UserSchema)
def user_object(pk: int, db: Session = Depends(get_db)):
    return user_crud.get(db, id=pk)

@router.delete("/delete/{pk}", response_model=UserSchema)
def user_object(pk: int, db: Session = Depends(get_db)):
    return user_crud.remove(db, id=pk)