from typing import List

from app.exceptions import DeviceAlreadyPairedException, DeviceInUseException, DeviceNotFoundException
from app.repository.device import DeviceRepository
from app.schemas.device import DeviceCreateSchema, DeviceSchema


class DeviceService:

    def __init__(self, device_repository: DeviceRepository):
        self.device_repository = device_repository

    def create_device(self, device_to_create: DeviceCreateSchema):
        return self.device_repository.create(device_to_create)

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
