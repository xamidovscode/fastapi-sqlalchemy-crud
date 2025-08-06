from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.crud.base import CRUDBase

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    async def get_user_by_email(self, db: AsyncSession, email: str):
        """Custom method to get a user by email, not covered by generic CRUD."""
        result = await db.execute(select(self.model).filter(self.model.email == email))
        return result.scalars().first()

    async def create(self, db: AsyncSession, *, obj_in: UserCreate) -> User:
        """Override create to handle password hashing (example)."""
        # In a real app, you'd hash the password here
        db_obj = self.model(email=obj_in.email, hashed_password=obj_in.password + "notreallyhashed")
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

user_crud = CRUDUser(User)
