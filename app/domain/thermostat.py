from app.domain.base import Device


class ThermostatDevice(Device):

    def __init__(self, id):
        super().__init__(id)

    def update_state(self, new_state):
        if not isinstance(new_state, (int, float)):
            raise TypeError("Thermostat state must be a number")
        if not (0 <= new_state <= 100):
            raise ValueError("Thermostat state must be between 0 and 100")
        return {"temperature": new_state}

    def get_default_state(self):
        return {"temperature": 24}
