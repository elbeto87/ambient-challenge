from http import HTTPStatus
from uuid import uuid4

from app.schemas.dwelling import DwellingCreateSchema, DwellingSchema, DwellingUpdateSchema


class TestDwelling:

    def test_create_new_dwelling(self, client):
        dwelling_to_create = DwellingCreateSchema(
            address="123 Main St",
            occupied=False
        )
        response = client.post("/v1/dwellings/create", json=dwelling_to_create.model_dump())
        response_json = response.json()

        assert response.status_code == HTTPStatus.CREATED
        assert response_json["address"] == dwelling_to_create.address
        assert response_json["occupied"] == dwelling_to_create.occupied

    def test_get_all_dwellings(self, client):
        response = client.get("/v1/dwellings")

        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.json(), list)

    def test_get_dwelling_success(self, client):
        create_data = DwellingCreateSchema(address="456 Elm St")
        create_resp = client.post("/v1/dwellings/create", json=create_data.model_dump())
        dwelling_id = create_resp.json()["id"]

        response = client.get(f"/v1/dwellings/{dwelling_id}")

        assert response.status_code == HTTPStatus.OK
        assert response.json()["id"] == dwelling_id

    def test_get_dwelling_not_found(self, client):
        invalid_id = str(uuid4())
        response = client.get(f"/v1/dwellings/{invalid_id}")

        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_update_occupied_status_success(self, client):
        create_data = DwellingCreateSchema(address="789 Pine St")
        create_resp = client.post("/v1/dwellings/create", json=create_data.model_dump())
        dwelling_id = create_resp.json()["id"]

        update_data = DwellingUpdateSchema(occupied=True)
        response = client.put(f"/v1/dwellings/{dwelling_id}", json=update_data.model_dump())

        assert response.status_code == HTTPStatus.OK


    def test_update_occupied_status_not_found(self, client):
        invalid_id = str(uuid4())
        update_data = DwellingUpdateSchema(occupied=True)

        response = client.put(f"/v1/dwellings/{invalid_id}", json=update_data.model_dump())
        assert response.status_code == HTTPStatus.NOT_FOUND
