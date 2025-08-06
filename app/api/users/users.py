from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import User, UserCreate, UserUpdate
from app.crud.user import user_crud # Import the instantiated user_crud
from app.core.database import get_db

router = APIRouter()

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await user_crud.get_user_by_email(db, email=user_in.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return await user_crud.create(db=db, obj_in=user_in)

@router.get("/", response_model=List[User])
async def read_users(
    db: AsyncSession = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    users = await user_crud.get_multi(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=User)
async def read_user_by_id(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await user_crud.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=User)
async def update_user(
    user_id: int,
    user_in: UserUpdate,
    db: AsyncSession = Depends(get_db)
):
    db_user = await user_crud.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    updated_user = await user_crud.update(db=db, db_obj=db_user, obj_in=user_in)
    return updated_user

@router.delete("/{user_id}", response_model=User)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    db_user = await user_crud.remove(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user
