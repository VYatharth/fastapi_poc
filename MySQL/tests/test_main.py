from fastapi.testclient import TestClient


def test_index(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "navigate to /docs route for open API spec"
