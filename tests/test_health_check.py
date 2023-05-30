from fastapi import status
from fastapi.testclient import TestClient

from api_example_poe.app.app import app

client = TestClient(app)


def test_health_check() -> None:
    resp = client.get("/health_check")
    assert resp.status_code == status.HTTP_200_OK
    assert resp.json() == {"status": "fine"}
