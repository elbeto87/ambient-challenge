from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Hub(BaseModel):
    __tablename__ = 'hubs'

    name = Column(String, nullable=False)
    dwelling_id = Column(ForeignKey("dwelling.id"))
    dwelling = relationship("Dwelling", back_populates="hubs")
    devices = relationship("Device", back_populates="hub")