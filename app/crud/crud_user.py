from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase, ModelType
from ..models.user import User
from ..schemas.user import UserSchema, UserCrudSchema


class CRUDUser(CRUDBase[User, UserCrudSchema, UserCrudSchema]):

    def remove(self, db: Session, **filters) -> Optional[ModelType]:
        obj = db.query(self.model).filter_by(**filters).first()

        if not obj:
            raise HTTPException(status_code=404, detail="Object not found")

        db.delete(obj)
        db.commit()
        return obj

user_crud = CRUDUser(User)
