from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from datetime import datetime, timedelta

from app.services.data_service import DataService
from app.services.prediction_service import PredictionService
from app.services.segmentation_service import SegmentationService

router = APIRouter()
data_service = DataService()
prediction_service = PredictionService()
segmentation_service = SegmentationService()

@router.get("/kpis")
async def get_dashboard_kpis():
    """
    Get main KPIs for dashboard
    """
    try:
        kpis = {
            "total_customers": data_service.get_total_customers(),
            "avg_churn_rate": prediction_service.get_average_churn_rate(),
            "high_risk_customers": prediction_service.get_high_risk_count(),
            "total_revenue_at_risk": data_service.get_revenue_at_risk(),
            "active_retention_campaigns": 4,
            "monthly_savings": 125000,
            "roi_percentage": 342,
            "customer_retention_rate": 85.7
        }
        return kpis
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/churn/trend")
async def get_churn_trend(days: int = 30):
    """
    Get churn rate trend over time
    """
    try:
        trend_data = prediction_service.get_churn_trend(days)
        return {
            "labels": [d["date"] for d in trend_data],
            "values": [d["churn_rate"] for d in trend_data]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/segment/performance")
async def get_segment_performance():
    """
    Get performance metrics by segment
    """
    try:
        performance = segmentation_service.get_segment_performance()
        return performance
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/revenue/impact")
async def get_revenue_impact():
    """
    Get revenue impact of retention strategies
    """
    try:
        impact = data_service.get_retention_revenue_impact()
        return impact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/prediction/distribution")
async def get_prediction_distribution():
    """
    Get distribution of churn predictions
    """
    try:
        distribution = prediction_service.get_prediction_distribution()
        return distribution
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/recent/activity")
async def get_recent_activity(limit: int = 10):
    """
    Get recent system activity
    """
    try:
        activities = data_service.get_recent_activities(limit)
        return {"activities": activities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))