from typing import List

from app.domain.base import Device
from app.exceptions import DeviceInUseException, DeviceNotFoundException
from app.repository.device import DeviceRepository
from app.schemas.device import DeviceCreateSchema, DeviceSchema, DeviceStateSchema, DeviceUpdateStateSchema


class DeviceService:

    def __init__(self, device_repository: DeviceRepository):
        self.device_repository = device_repository

    def create_device(self, device_to_create: DeviceCreateSchema):
        device_model = self.device_repository.create(device_to_create)
        default_state = Device.from_orm(device_model).get_default_state()
        self.device_repository.update_state(device_model.id, default_state)
        return DeviceSchema.from_orm(device_model)

    def delete_device(self, device_id: str):
        device = self.device_repository.get_device_by_id(device_id)
        if not device:
            raise DeviceNotFoundException(device_id)
        if device.hub:
            raise DeviceInUseException(device_id)
        return self.device_repository.delete(device_id)

    def get_all_devices(self) -> List[DeviceSchema]:
        devices = self.device_repository.get_all_devices()
        return [DeviceSchema.model_validate(device) for device in devices] if devices else []

    def get_device_state(self, device_id: str) -> DeviceStateSchema:
        device = self.device_repository.get_device_by_id(device_id)
        if not device:
            raise DeviceNotFoundException(device_id)
        return DeviceStateSchema.model_validate(device).state

    def modify_device_state(self, device_id: str, device_state: DeviceUpdateStateSchema) -> DeviceStateSchema:
        device_model = self.device_repository.get_device_by_id(device_id)
        if not device_model:
            raise DeviceNotFoundException(device_id)
        device = Device.from_orm(device_model)
        new_state = device.update_state(device_state.state)
        return self.device_repository.update_state(device_id, new_state)
