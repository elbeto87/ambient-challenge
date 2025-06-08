from sqlalchemy.orm import Session

from app.models.dwellingmodel import DwellingModel
from app.schemas.dwellingschema import DwellingSchema


class DwellingRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, dwelling_to_add: DwellingSchema):
        dwelling_model = DwellingModel(
            address=dwelling_to_add.address,
            occupied=dwelling_to_add.occupied
        )
        self.db.add(dwelling_model)
        self.db.commit()
        return dwelling_model

    def get_by_id(self, dwelling_id: int):
        return self.db.query(DwellingModel).filter(DwellingModel.id == dwelling_id).first()
