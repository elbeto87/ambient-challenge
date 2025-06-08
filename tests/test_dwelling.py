from http import HTTPStatus

from app.schemas.dwelling import DwellingCreateSchema


class TestDwelling:

    def test_create_new_dwelling(self, client):
        dwelling_to_create = DwellingCreateSchema(
            address="123 Main St",
            occupied=False
        )
        response = client.post("/v1/dwellings/create", json=dwelling_to_create.model_dump())

        assert response.status_code == HTTPStatus.OK
        assert response.json() == dwelling_to_create.model_dump()

    def test_get_all_dwellings(self, client):
        response = client.get("/v1/dwellings")

        assert response.status_code == HTTPStatus.OK
