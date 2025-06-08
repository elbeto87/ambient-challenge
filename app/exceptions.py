class DwellingNotFoundException(Exception):

    def __init__(self, dwelling_id: str):
        super().__init__(f"Dwelling with id {dwelling_id} not found")
