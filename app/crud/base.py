from typing import Generic, TypeVar, Type, List, Optional, Dict, Any

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from ..core.database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, **filters) -> Optional[ModelType]:
        """Generic get method to filter by any field"""
        return db.query(self.model).filter_by(**filters).first()

    def list(self, db: Session, skip: Optional[int], limit: Optional[int]) -> List[ModelType]:
        return db.query(self.model).offset(skip).limit(limit).all()

    def create(self, db: Session, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType | Dict[str, Any]
    ) -> ModelType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        for field in update_data:
            setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db: Session, **filters) -> Optional[ModelType]:
        obj = db.query(self.model).filter_by(**filters).first()

        if not obj:
            raise HTTPException(status_code=404, detail="Object not found")

        db.delete(obj)
        db.commit()
        return obj
