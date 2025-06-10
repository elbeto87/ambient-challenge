from typing import List

from app.exceptions import DwellingNotFoundException, HubNotFoundException
from app.repository.dwelling import DwellingRepository
from app.repository.hub import HubRepository
from app.schemas.dwelling import DwellingCreateSchema, DwellingUpdateSchema, DwellingSchema


class DwellingService:

    def __init__(self, dwelling_repository: DwellingRepository, hub_repository: HubRepository):
        self.dwelling_repository = dwelling_repository
        self.hub_repository = hub_repository

    def create_dwelling(self, dwelling_to_add: DwellingCreateSchema) -> DwellingSchema:
        dwelling = self.dwelling_repository.create(dwelling_to_add)
        return DwellingSchema.from_orm(dwelling)

    def get_dwelling(self, dwelling_id: str) -> DwellingSchema:
        dwelling = self.dwelling_repository.get_by_id(dwelling_id)
        if not dwelling:
            raise DwellingNotFoundException(dwelling_id)
        return DwellingSchema.model_validate(dwelling)

    def get_all_dwellings(self) -> List[DwellingSchema]:
        dwellings = self.dwelling_repository.get_all()
        return [DwellingSchema.model_validate(dwelling) for dwelling in dwellings] if dwellings else []

    def update_dwelling(self, dwelling_id: str, dwelling_status: DwellingUpdateSchema) -> DwellingUpdateSchema:
        dwelling = self.dwelling_repository.update(dwelling_id, dwelling_status)
        if not dwelling:
            raise DwellingNotFoundException(dwelling_id)
        return DwellingSchema.model_validate(dwelling)

    def install_hub(self, dwelling_id: str, hub_to_install: str):
        dwelling = self.dwelling_repository.get_by_id(dwelling_id)
        hub = self.hub_repository.get_by_id(hub_to_install)
        if not dwelling:
            raise DwellingNotFoundException(dwelling_id)
        if not hub:
            raise HubNotFoundException(hub_to_install)
        return self.dwelling_repository.add_new_hub(dwelling, hub)
