from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from app.database.base import Base


class Dwelling(Base):
    address = Column(String, nullable=False)
    occupied = Column(Boolean, default=False)
    hubs = relationship("Hub", back_populates="dwelling")
