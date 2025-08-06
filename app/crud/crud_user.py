from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate

class CRUDUser:
    async def get_user_by_email(self, db: AsyncSession, email: str):
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    async def create_user(self, db: AsyncSession, user: UserCreate):
        # In a real app, you'd hash the password here
        db_user = User(email=user.email, hashed_password=user.password + "notreallyhashed")
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user

user_crud = CRUDUser()
