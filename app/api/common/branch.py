from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.schemas.branch import (
    BranchListSchema, BranchCreateSchema
)
from app.crud.branch import branch_crud

router = APIRouter()

@router.post("/create/", response_model=BranchListSchema, status_code=status.HTTP_201_CREATED)
async def create_branch(data: BranchCreateSchema, db: AsyncSession = Depends(get_db)):
    return await branch_crud.create(db=db, data=data)


@router.get("/list/", response_model=List[BranchListSchema], status_code=status.HTTP_200_OK)
async def list_branches(skip: int = None, limit: int = None, db: AsyncSession = Depends(get_db)):
    return await branch_crud.get_multi(db=db, skip=skip, limit=limit)
