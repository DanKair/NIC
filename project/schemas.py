from datetime import datetime

from pydantic import BaseModel
from typing import Optional

# Schema for reading an item
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# Schema for creating an item
class ItemCreate(ItemBase):
    pass

# Schema for showing an item in responses
class ItemResponse(ItemBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
