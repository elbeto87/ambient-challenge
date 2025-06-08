from pydantic import BaseModel

class DwellingSchema(BaseModel):
    address: str
    occupied: bool = False

    class Config:
        orm_mode = True
