import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_retention_strategies():
    response = client.get("/api/retention/strategies/0")
    assert response.status_code == 200
    data = response.json()
    assert "strategies" in data