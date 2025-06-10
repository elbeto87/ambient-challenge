from typing import Optional, List

from pydantic import BaseModel
from uuid import UUID

from app.schemas.device import DeviceSchema


class HubCreateSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True

class HubSchema(BaseModel):
    id: UUID
    name: str
    dwelling_id: Optional[UUID]
    devices: List[DeviceSchema] = []

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
