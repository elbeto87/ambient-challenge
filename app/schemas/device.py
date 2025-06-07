from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from .base import BaseSchema
from enum import Enum

class DeviceType(str, Enum):
    SWITCH = "switch"
    DIMMER = "dimmer"
    LOCK = "lock"
    THERMOSTAT = "thermostat"

class DeviceCreate(BaseModel):
    name: str
    type: DeviceType
    pin_code: Optional[str] = None  # For locks only

class DeviceUpdate(BaseModel):
    state: Optional[str]
    pin_code: Optional[str]

class DeviceOut(BaseSchema):
    name: str
    type: DeviceType
    state: Optional[str]
    pin_code: Optional[str]
    hub_id: Optional[UUID]
