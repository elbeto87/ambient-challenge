from sqlalchemy.orm import Session

from app.models import DeviceModel
from app.schemas.device import DeviceCreateSchema


class DeviceRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, device_to_create: DeviceCreateSchema) -> DeviceModel:
        device_model = DeviceModel(name=device_to_create.name, type=device_to_create.type)
        self.db.add(device_model)
        self.db.commit()
        return device_model
