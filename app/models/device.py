from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

from app.database.base import Base
from app.models.base import BaseModel


class DeviceType(str, PyEnum):
    SWITCH = "switch"
    DIMMER = "dimmer"
    LOCK = "lock"
    THERMOSTAT = "thermostat"

class Device(BaseModel):
    name = Column(String, nullable=False)
    type = Column(Enum(DeviceType), nullable=False)
    state = Column(String, nullable=True)  # Could be 'on', 'off', intensity %, temperature, etc.
    pin_code = Column(String, nullable=True)  # Only for lock
    hub_id = Column(ForeignKey("hub.id"), nullable=True)
    hub = relationship("Hub", back_populates="devices")