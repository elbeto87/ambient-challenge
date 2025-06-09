from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as PyEnum

from app.models.base import BaseModel


class DeviceType(str, PyEnum):
    SWITCH = "switch"
    DIMMER = "dimmer"
    LOCK = "lock"
    THERMOSTAT = "thermostat"

class DeviceModel(BaseModel):
    __tablename__ = 'devices'

    name = Column(String, nullable=False)
    type = Column(Enum(DeviceType), nullable=False)
    state = Column(String, nullable=True)
    pin_code = Column(String, nullable=True)
    hub_id = Column(ForeignKey("hubs.id"), nullable=True)
    hub = relationship("HubModel", back_populates="devices")