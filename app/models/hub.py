from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database.base import Base
from app.models.base import BaseModel


class Hub(BaseModel):
    name = Column(String, nullable=False)
    dwelling_id = Column(ForeignKey("dwelling.id"))
    dwelling = relationship("Dwelling", back_populates="hubs")
    devices = relationship("Device", back_populates="hub")