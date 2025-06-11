from typing import Optional, Any, Dict
from pydantic import BaseModel, field_validator
import json
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

    @field_validator("state", mode="before")
    @classmethod
    def parse_state(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return {}
        return v

    class Config:
        from_attributes = True
