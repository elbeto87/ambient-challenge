from app.repository.dwelling import DwellingRepository
from app.schemas.dwellingschema import DwellingSchema


class DwellingService:

    def __init__(self, dwelling_repository: DwellingRepository):
        self.dwelling_repository = dwelling_repository

    def create_dwelling(self, dwelling_to_add: DwellingSchema):
        dwelling = self.dwelling_repository.create(dwelling_to_add)
        return DwellingSchema.model_validate(dwelling)

    def get_dwelling(self, dwelling_id: int):
        dwelling = self.dwelling_repository.get_by_id(dwelling_id)
        return DwellingSchema.model_validate(dwelling)
