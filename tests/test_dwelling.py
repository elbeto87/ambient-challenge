from app.schemas.dwelling import DwellingSchema


class TestDwelling:

    def test_create_new_dwelling(self, client):
        dwelling_to_create = DwellingSchema(
            address="123 Main St",
            occupied=False
        )
        response = client.post("/dwelling", json=dwelling_to_create.model_dump())
        breakpoint()
        assert response.status_code == 200
        assert response.json() == {"message": "Dwelling created successfully."}

    def test_get_all_dwellings(self, client):
        response = client.get("/dwellings")
        assert response.status_code == 200
