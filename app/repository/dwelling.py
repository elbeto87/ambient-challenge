from uuid import UUID

from sqlalchemy.orm import Session

from app.models import HubModel
from app.models.dwelling import DwellingModel
from app.schemas.dwelling import DwellingCreateSchema, DwellingUpdateSchema


class DwellingRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, dwelling_to_add: DwellingCreateSchema):
        dwelling_model = DwellingModel(
            address=dwelling_to_add.address,
            occupied=dwelling_to_add.occupied
        )
        self.db.add(dwelling_model)
        self.db.commit()
        return dwelling_model

    def get_by_id(self, dwelling_id: str):
        return self.db.query(DwellingModel).filter(DwellingModel.id == UUID(dwelling_id)).first()

    def get_all(self):
        return self.db.query(DwellingModel).all()

    def update(self, dwelling_id: str, dwelling_occupied_status: DwellingUpdateSchema):
        dwelling = self.get_by_id(dwelling_id)
        if not dwelling:
            return None
        dwelling.occupied = dwelling_occupied_status.occupied
        self.db.commit()
        return dwelling

    def add_new_hub(self, dwelling: DwellingModel, hub_to_install: HubModel):
        dwelling.hubs.append(hub_to_install)
        self.db.commit()
        return dwelling
