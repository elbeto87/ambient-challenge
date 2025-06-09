from abc import ABC, abstractmethod

from app.domain.dimmer import DimmerDevice
from app.domain.lock import LockDevice
from app.domain.switch import SwitchDevice
from app.domain.thermostat import ThermostatDevice
from app.models import DeviceModel


class Device(ABC):

    def __init__(self, id: str):
        self.id = id

    @classmethod
    def from_orm(cls, device_model: DeviceModel):
        device_type = device_model.type
        device_type_map = {
            "switch": SwitchDevice,
            "dimmer": DimmerDevice,
            "lock": LockDevice,
            "thermostat": ThermostatDevice
        }
        device_type = device_type_map[device_type]
        return device_type(id=device_model.id)

    @abstractmethod
    def update_state(self, new_state: any):
        raise NotImplementedError()

    @abstractmethod
    def get_default_state(self):
        raise NotImplementedError()
