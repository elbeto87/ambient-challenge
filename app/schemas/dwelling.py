from uuid import UUID

from pydantic import BaseModel


class DwellingCreateSchema(BaseModel):
    address: str
    occupied: bool = False

    class Config:
        from_attributes = True


class DwellingSchema(BaseModel):
    id: UUID
    address: str
    occupied: bool = False

    class Config:
        from_attributes = True


class DwellingUpdateSchema(BaseModel):
    occupied: bool

    class Config:
        from_attributes = True
