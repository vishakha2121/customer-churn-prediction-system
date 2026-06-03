import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_churn():
    response = client.post("/api/churn/predict", json={
        "customer_id": "TEST001",
        "tenure_months": 12,
        "monthly_charges": 70.5,
        "total_charges": 846,
        "contract_type": "Month-to-month",
        "payment_method": "Electronic check",
        "paperless_billing": True,
        "internet_service": "Fiber optic",
        "online_security": "No",
        "online_backup": "No",
        "device_protection": "No",
        "tech_support": "No",
        "streaming_tv": "Yes",
        "streaming_movies": "Yes"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert "churn_probability" in data
    assert "risk_level" in data

def test_get_model_accuracy():
    response = client.get("/api/churn/model/accuracy")
    assert response.status_code == 200
    data = response.json()
    assert "accuracy" in data