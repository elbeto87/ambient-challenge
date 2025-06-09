from app.repository.device import DeviceRepository
from app.schemas.device import DeviceCreateSchema


class DeviceService:

    def __init__(self, device_repository: DeviceRepository):
        self.device_repository = device_repository

    def create_device(self, device_to_create: DeviceCreateSchema):
        return self.device_repository.create(device_to_create)