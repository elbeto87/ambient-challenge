from app.exceptions import HubNotFoundException, DeviceAlreadyPairedException, DeviceNotFoundException
from app.repository.hub import HubRepository
from app.schemas.hub import HubCreateSchema, HubSchema


class HubService:

    def __init__(self, hub_repository: HubRepository):
        self.hub_repository = hub_repository

    def create_hub(self, hub_to_add: HubCreateSchema):
        hub = self.hub_repository.create(hub_to_add)
        return HubCreateSchema.from_orm(hub)

    def get_devices(self, hub_id: str):
        hub = self.hub_repository.get_by_id(hub_id)
        if not hub:
            raise HubNotFoundException(hub_id)
        return [device.model_dump() for device in hub.devices]

    def delete_device(self, hub_id: str, device_to_delete: str):
        hub = self.hub_repository.get_by_id(hub_id)
        if not hub:
            raise HubNotFoundException(hub_id)
        if device_to_delete not in hub.devices:
            raise DeviceNotFoundException(device_to_delete)
        return self.hub_repository.delete_device_from_hub(hub, device_to_delete)

    def pair_device(self, hub_id: str, device_to_pair: str):
        hub = self.hub_repository.get_by_id(hub_id)
        if not hub:
            raise HubNotFoundException(hub_id)
        if device_to_pair in hub.devices:
            raise DeviceAlreadyPairedException(device_to_pair)
        self.hub_repository.add_device_to_hub(hub, device_to_pair)
        return {"message": "Device paired successfully", "device": device_to_pair}

    def get_device_status(self, hub_id: str, device_id: str):
        hub = self.hub_repository.get_by_id(hub_id)
        if not hub:
            raise HubNotFoundException(hub_id)
        if device_id not in hub.devices:
            raise DeviceNotFoundException(device_id)
        return hub.devices[device_id].status

    def get_all_hubs(self):
        hubs = self.hub_repository.get_all_hubs()
        return [HubSchema.model_validate(hub) for hub in hubs]
