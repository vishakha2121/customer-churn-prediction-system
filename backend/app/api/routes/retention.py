from fastapi import APIRouter, HTTPException
from typing import List, Dict, Any

from app.services.segmentation_service import SegmentationService
from app.core.retention.strategy_engine import StrategyEngine
from app.core.retention.offer_generator import OfferGenerator

router = APIRouter()
segmentation_service = SegmentationService()
strategy_engine = StrategyEngine()
offer_generator = OfferGenerator()

@router.get("/strategies/{segment_id}")
async def get_retention_strategies(segment_id: int):
    """
    Get recommended retention strategies for a specific segment
    """
    try:
        strategies = strategy_engine.generate_strategies_for_segment(segment_id)
        return {
            "segment_id": segment_id,
            "strategies": strategies
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/strategies/customize")
async def customize_strategy(
    segment_id: int,
    budget_constraint: float = None,
    timeline_days: int = 30
):
    """
    Customize retention strategies based on constraints
    """
    try:
        customized = strategy_engine.customize_strategy(
            segment_id=segment_id,
            budget=budget_constraint,
            timeline=timeline_days
        )
        return customized
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/offers/{segment_id}")
async def get_offers_for_segment(segment_id: int, limit: int = 5):
    """
    Get specific offers for a customer segment
    """
    try:
        offers = offer_generator.generate_offers(segment_id, limit)
        return {
            "segment_id": segment_id,
            "offers": offers
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/offers/apply")
async def apply_offer(customer_id: str, offer_id: str):
    """
    Apply a specific offer to a customer
    """
    try:
        result = offer_generator.apply_offer(customer_id, offer_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/strategies/compare")
async def compare_strategies(segment_ids: str):
    """
    Compare strategies across multiple segments
    """
    try:
        ids = [int(id) for id in segment_ids.split(",")]
        comparison = strategy_engine.compare_strategies(ids)
        return comparison
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))