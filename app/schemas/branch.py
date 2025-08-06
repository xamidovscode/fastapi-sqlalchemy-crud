from typing import Optional
from pydantic import BaseModel
from datetime import time

class BranchCreateSchema(BaseModel):
    name: str
    start_time: time
    end_time: time
    is_active: bool = True

    class Config:
        orm_mode = True


class BranchListSchema(BaseModel):
    id: int
    name: str
    start_time: time
    end_time: time
    is_active: bool = True