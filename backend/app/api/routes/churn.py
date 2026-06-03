from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict, Any
import pandas as pd
import numpy as np

from app.api.models.churn_request import ChurnPredictionRequest, BatchPredictionRequest
from app.services.prediction_service import PredictionService
from app.database.crud import CRUDOperations
from app.utils.validators import validate_customer_data

router = APIRouter()
prediction_service = PredictionService()
db_ops = CRUDOperations()

@router.post("/predict")
async def predict_churn(request: ChurnPredictionRequest):
    """
    Predict churn probability for a single customer
    """
    try:
        # Convert request to dict
        customer_data = request.model_dump()
        
        # Validate input
        validation_result = validate_customer_data(customer_data)
        if not validation_result["valid"]:
            raise HTTPException(status_code=400, detail=validation_result["errors"])
        
        # Make prediction
        prediction = prediction_service.predict_single(customer_data)
        
        # Save to database
        db_ops.save_prediction(customer_data, prediction)
        
        return {
            "customer_id": request.customer_id,
            "churn_probability": round(prediction["probability"] * 100, 2),
            "risk_level": prediction["risk_level"],
            "prediction_date": prediction["timestamp"],
            "confidence_score": prediction["confidence"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict/batch")
async def predict_batch(request: BatchPredictionRequest):
    """
    Predict churn probability for multiple customers
    """
    try:
        customers_data = [customer.model_dump() for customer in request.customers]
        predictions = prediction_service.predict_batch(customers_data)
        
        return {
            "total_customers": len(predictions),
            "high_risk_count": sum(1 for p in predictions if p["risk_level"] == "High"),
            "medium_risk_count": sum(1 for p in predictions if p["risk_level"] == "Medium"),
            "low_risk_count": sum(1 for p in predictions if p["risk_level"] == "Low"),
            "predictions": predictions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/model/accuracy")
async def get_model_accuracy():
    """
    Get current model performance metrics
    """
    try:
        metrics = prediction_service.get_model_metrics()
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/features/importance")
async def get_feature_importance():
    """
    Get feature importance scores
    """
    try:
        importance = prediction_service.get_feature_importance()
        return {"features": importance}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))