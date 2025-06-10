from typing import Optional, Any, Dict
from pydantic import BaseModel
from uuid import UUID
from .base import BaseSchema
from enum import Enum

class DeviceType(str, Enum):
    SWITCH = "switch"
    DIMMER = "dimmer"
    LOCK = "lock"
    THERMOSTAT = "thermostat"


class DeviceCreateSchema(BaseModel):
    name: str
    type: DeviceType

    class Config:
        from_attributes = True


class DeviceUpdateStateSchema(BaseModel):
    state: Any

    class Config:
        from_attributes = True


class DeviceStateSchema(BaseModel):
    id: UUID
    name: str
    type: DeviceType
    state: Optional[Dict[str, Any]]

    class Config:
        from_attributes = True


class DeviceSchema(BaseSchema):
    name: str
    type: DeviceType
    state: Optional[Dict[str, Any]]
    hub_id: Optional[UUID]

    class Config:
        from_attributes = True
