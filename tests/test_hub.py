import pytest
from http import HTTPStatus

from app.schemas.hub import HubCreateSchema


def test_get_all_hubs(client):
    response = client.get("/v1/hub/")
    response_json = response.json()

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response_json, list)


def test_create_hub(client):
    new_hub = HubCreateSchema(name="New Hub")
    response = client.post("/v1/hub/", json=new_hub.model_dump())
    response_json = response.json()

    assert response.status_code == HTTPStatus.CREATED
    assert response_json["name"] == new_hub.name
