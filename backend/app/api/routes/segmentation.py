from fastapi import APIRouter, HTTPException, Query
from typing import List, Dict, Any

from app.services.segmentation_service import SegmentationService
from app.database.crud import CRUDOperations

router = APIRouter()
segmentation_service = SegmentationService()
db_ops = CRUDOperations()

@router.get("/segments")
async def get_all_segments():
    """
    Get all customer segments with their characteristics
    """
    try:
        segments = segmentation_service.get_segments_summary()
        return {"segments": segments}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/segment/{segment_id}")
async def get_segment_details(segment_id: int):
    """
    Get detailed information about a specific segment
    """
    try:
        segment = segmentation_service.get_segment_by_id(segment_id)
        if not segment:
            raise HTTPException(status_code=404, detail="Segment not found")
        return segment
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/assign")
async def assign_customer_to_segment(customer_id: str):
    """
    Assign a customer to appropriate segment based on their features
    """
    try:
        segment = segmentation_service.assign_customer_to_segment(customer_id)
        return {
            "customer_id": customer_id,
            "segment_id": segment["segment_id"],
            "segment_name": segment["segment_name"],
            "churn_risk_in_segment": segment["avg_churn_rate"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/distribution")
async def get_segment_distribution():
    """
    Get distribution of customers across segments
    """
    try:
        distribution = segmentation_service.get_segment_distribution()
        return distribution
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/characteristics/{segment_id}")
async def get_segment_characteristics(segment_id: int):
    """
    Get detailed characteristics of a segment
    """
    try:
        characteristics = segmentation_service.get_segment_characteristics(segment_id)
        return characteristics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))