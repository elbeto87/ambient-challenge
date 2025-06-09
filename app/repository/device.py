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

    def get_device_by_id(self, device_id: str) -> DeviceModel:
        return self.db.query(DeviceModel).filter(DeviceModel.id == device_id).first()

    def delete(self, device_id: str) -> DeviceModel:
        device = self.get_device_by_id(device_id)
        self.db.delete(device)
        self.db.commit()
        return device

    def get_all_devices(self) -> list[DeviceModel]:
        return self.db.query(DeviceModel).all()

    def update_state(self, device_id: str, new_state: any) -> DeviceModel:
        device = self.get_device_by_id(device_id)
        device.state = new_state
        self.db.commit()
        return device
