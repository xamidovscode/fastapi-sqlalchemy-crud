from fastapi import APIRouter
from app.api.users import users
from app.api.common import (
    branch, course, payment_type, role, room, setting, source, weekend
)

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(branch.router, prefix="/branches", tags=["branches"])
api_router.include_router(course.router, prefix="/courses", tags=["courses"])
api_router.include_router(payment_type.router, prefix="/payment_types", tags=["payment_types"])
api_router.include_router(role.router, prefix="/roles", tags=["roles"])
api_router.include_router(room.router, prefix="/rooms", tags=["rooms"])
api_router.include_router(setting.router, prefix="/settings", tags=["settings"])
api_router.include_router(source.router, prefix="/sources", tags=["sources"])
api_router.include_router(weekend.router, prefix="/weekends", tags=["weekends"])
