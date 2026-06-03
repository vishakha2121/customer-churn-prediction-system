import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_all_segments():
    response = client.get("/api/segmentation/segments")
    assert response.status_code == 200
    data = response.json()
    assert "segments" in data

def test_get_segment_details():
    response = client.get("/api/segmentation/segment/0")
    assert response.status_code == 200
    data = response.json()
    assert "segment_id" in data