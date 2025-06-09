from typing import Optional

from pydantic import BaseModel
from uuid import UUID

class HubCreateSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True

class HubSchema(BaseModel):
    id: UUID
    name: str
    dwelling_id: Optional[UUID]
    devices: list[UUID] = []

    class Config:
        from_attributes = True

class DeviceToDeleteSchema(BaseModel):
    device_id: UUID

    class Config:
        from_attributes = True

class DeviceToPairSchema(BaseModel):
    device_id: UUID

    class Config:
        from_attributes = True
