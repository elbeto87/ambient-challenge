class DwellingNotFoundException(Exception):

    def __init__(self, dwelling_id: str):
        super().__init__(f"Dwelling with id {dwelling_id} not found")


class HubNotFoundException(Exception):

    def __init__(self, hub_id: str):
        super().__init__(f"Hub with id {hub_id} not found")


class DeviceAlreadyPairedException(Exception):

    def __init__(self, device_id: str):
        super().__init__(f"Device with id {device_id} is already paired with a hub")


class DeviceNotFoundException(Exception):

    def __init__(self, device_id: str):
        super().__init__(f"Device with id {device_id} not found")


class DeviceInUseException(Exception):

    def __init__(self, device_id: str):
        super().__init__(f"Device with id {device_id} is currently in use and cannot be deleted")

