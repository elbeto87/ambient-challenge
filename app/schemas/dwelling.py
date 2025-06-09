from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel

from app.schemas.hub import HubSchema


class DwellingCreateSchema(BaseModel):
    address: str
    occupied: bool = False

    class Config:
        from_attributes = True


class DwellingSchema(BaseModel):
    id: UUID
    address: str
    occupied: bool = False
    hubs: List[HubSchema] = []

    class Config:
        from_attributes = True


class DwellingUpdateSchema(BaseModel):
    occupied: bool

    class Config:
        from_attributes = True


class InstallHubSchema(BaseModel):
    hub_id: UUID
