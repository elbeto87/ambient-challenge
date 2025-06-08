from pydantic import BaseModel

class DwellingSchema(BaseModel):
    address: str
    occupied: bool = False

    class Config:
        from_attributes = True


class DwellingUpdateSchema(BaseModel):
    occupied: bool
