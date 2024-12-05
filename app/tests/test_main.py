from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_rooms():
    response = client.get("/api/v1/rooms")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
