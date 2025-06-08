from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class HubModel(BaseModel):
    __tablename__ = 'hubs'

    name = Column(String, nullable=False)
    dwelling_id = Column(ForeignKey("dwellings.id"))
    dwelling = relationship("DwellingModel", back_populates="hubs")
    devices = relationship("DeviceModel", back_populates="hub")