from app.domain.base import Device


class DimmerDevice(Device):

    def __init__(self, id):
        super().__init__(id)

    def update_state(self, new_state):
        if not isinstance(new_state, (int, float)):
            raise TypeError("Dimmer state must be a number")
        if not (0 <= new_state <= 100):
            raise ValueError("Dimmer state must be between 0 and 100")
        return {"brightness": new_state}

    def get_default_state(self):
        return {"brightness": 10}
