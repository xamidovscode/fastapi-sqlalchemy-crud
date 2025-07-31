from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    full_name: str


class UserCrudSchema(BaseModel):
    full_name: str
