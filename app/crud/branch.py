from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from .base import CRUDBase
from app.models.branch import Branch
from app.schemas.branch import BranchListSchema, BranchCreateSchema

class CRUDBranch(CRUDBase[Branch, BranchCreateSchema, BranchListSchema]):

    async def create(self, db: AsyncSession, *, data: BranchCreateSchema) -> Branch:
        existing_branch = await branch_crud.get(db, name=data.name)
        if existing_branch:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"message": "A branch with that name already exists."},
            )
        branch = await super().create(db, data=data)
        return branch


branch_crud = CRUDBranch(Branch)