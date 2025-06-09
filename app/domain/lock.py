from app.domain.base import Device


class LockDevice(Device):

    def __init__(self, id):
        super().__init__(id)

    def update_state(self, new_state):
        if not isinstance(new_state, bool):
            raise TypeError("Lock state must be a boolean")
        return {"is_locked": new_state}

    def get_default_state(self):
        return {"is_locked": False}
