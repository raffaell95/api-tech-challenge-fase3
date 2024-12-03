from pydantic import BaseModel
from typing import Optional


class UDataSchema(BaseModel):
    id: Optional[int] = None
    user_id: str
    item_id: str
    rating: str
    timestamp: str

    class Config:
        orm_mode = True