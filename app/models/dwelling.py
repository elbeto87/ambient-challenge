from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class DwellingModel(BaseModel):
    __tablename__ = 'dwellings'

    address = Column(String, nullable=False)
    occupied = Column(Boolean, default=False)
    hubs = relationship("Hub", back_populates="dwelling")
