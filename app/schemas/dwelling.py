from typing import List, Optional
from .base import BaseSchema
from pydantic import BaseModel
from uuid import UUID

class DwellingCreate(BaseModel):
    address: str

class DwellingUpdate(BaseModel):
    occupied: Optional[bool]

class DwellingOut(BaseSchema):
    address: str
    occupied: bool
