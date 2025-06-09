from sqlalchemy.orm import Session

from app.models import HubModel
from app.schemas.hub import HubCreateSchema


class HubRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, hub_to_add: HubCreateSchema) -> HubModel:
        hub_model = HubModel(name=hub_to_add.name)
        self.db.add(hub_model)
        self.db.commit()
        return hub_model

    def get_by_id(self, hub_id: str) -> HubModel:
        return self.db.query(HubModel).filter(HubModel.id == hub_id).first()

    def delete_device_from_hub(self, hub: HubModel, device_to_delete: str):
        hub.devices.remove(device_to_delete)
        self.db.commit()
        return device_to_delete

    def add_device_to_hub(self, hub: HubModel, device_to_pair: str):
        hub.devices.append(device_to_pair)
        self.db.commit()
        return device_to_pair

    def get_all_hubs(self) -> list[HubModel]:
        return self.db.query(HubModel).all()
