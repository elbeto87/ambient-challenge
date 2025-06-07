from pydantic import BaseModel
from .base import BaseSchema
from uuid import UUID

class HubCreate(BaseModel):
    name: str
    dwelling_id: UUID

class HubOut(BaseSchema):
    name: str
    dwelling_id: UUID
