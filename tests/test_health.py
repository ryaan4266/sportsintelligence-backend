from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_returns_ok_status_code():
    response = client.get("/health")

    assert response.status_code == 200


def test_health_returns_service_status():
    response = client.get("/health")

    assert response.json() == {
        "status": "ok",
        "service": "Athena Sports Intelligence API",
    }
