from app.exceptions import DwellingNotFoundException
from app.repository.dwelling import DwellingRepository
from app.schemas.dwelling import DwellingSchema, DwellingUpdateSchema


class DwellingService:

    def __init__(self, dwelling_repository: DwellingRepository):
        self.dwelling_repository = dwelling_repository

    def create_dwelling(self, dwelling_to_add: DwellingSchema):
        dwelling = self.dwelling_repository.create(dwelling_to_add)
        return DwellingSchema.from_orm(dwelling)

    def get_dwelling(self, dwelling_id: int):
        dwelling = self.dwelling_repository.get_by_id(dwelling_id)
        if not dwelling:
            raise DwellingNotFoundException(dwelling_id)
        return DwellingSchema.model_validate(dwelling)

    def get_all_dwellings(self):
        dwellings = self.dwelling_repository.get_all()
        return [DwellingSchema.model_validate(dwelling) for dwelling in dwellings] if dwellings else []

    def update_dwelling(self, dwelling_id: int, dwelling_occupied_status: DwellingUpdateSchema):
        dwelling = self.dwelling_repository.update(dwelling_id, dwelling_occupied_status)
        if not dwelling:
            raise DwellingNotFoundException(dwelling_id)
        return DwellingSchema.model_validate(dwelling)
