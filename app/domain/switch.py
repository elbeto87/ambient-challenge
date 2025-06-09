from app.domain.base import Device


class SwitchDevice(Device):

    def __init__(self, id):
        super().__init__(id)

    def update_state(self, new_state):
        if not isinstance(new_state, bool):
            raise TypeError("Lock state must be a boolean")
        return {"is_open": new_state}

    def get_default_state(self):
        return {"is_open": False}
