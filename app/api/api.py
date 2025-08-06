from fastapi import APIRouter
from app.api.users import users
from app.api.common import (
    branch,
)

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(branch.router, prefix="/branches", tags=["branches"])
