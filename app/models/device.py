from sqlalchemy import Column, String, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from enum import Enum

from app.models.base import BaseModel


class DeviceType(str, Enum):
    SWITCH = "switch"
    DIMMER = "dimmer"
    LOCK = "lock"
    THERMOSTAT = "thermostat"

class DeviceModel(BaseModel):
    __tablename__ = 'devices'

    name = Column(String, nullable=False)
    type = Column(SQLAlchemyEnum(DeviceType), nullable=False)
    state = Column(JSONB().with_variant(JSONB, "sqlite"), nullable=False)
    hub_id = Column(ForeignKey("hubs.id"), nullable=True)
    hub = relationship("HubModel", back_populates="devices")
