from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from app.api.models.simulation_request import SimulationRequest
from app.services.simulation_service import SimulationService
from app.core.retention.roi_calculator import ROICalculator

router = APIRouter()
simulation_service = SimulationService()
roi_calculator = ROICalculator()

@router.post("/roi/simulate")
async def simulate_roi(request: SimulationRequest):
    """
    Simulate ROI for retention strategies
    """
    try:
        simulation_result = simulation_service.simulate_retention_impact(request)
        
        return {
            "simulation_id": simulation_result["id"],
            "expected_roi_percentage": simulation_result["roi_percentage"],
            "net_savings": simulation_result["net_savings"],
            "breakeven_months": simulation_result["breakeven_months"],
            "customers_saved": simulation_result["customers_saved"],
            "total_cost": simulation_result["total_cost"],
            "revenue_retained": simulation_result["revenue_retained"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/roi/scenario")
async def run_scenario_analysis(
    strategy_name: str,
    target_segment: int,
    investment_amount: float
):
    """
    Run what-if scenario analysis
    """
    try:
        scenarios = roi_calculator.run_scenario_analysis(
            strategy=strategy_name,
            segment_id=target_segment,
            investment=investment_amount
        )
        return scenarios
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/roi/historical/{strategy_id}")
async def get_historical_roi(strategy_id: int):
    """
    Get historical ROI data for a strategy
    """
    try:
        historical_data = roi_calculator.get_historical_roi(strategy_id)
        return historical_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/roi/optimize")
async def optimize_roi(
    target_roi: float = 20.0,
    max_budget: float = 100000
):
    """
    Optimize resource allocation for maximum ROI
    """
    try:
        optimized = roi_calculator.optimize_allocation(
            target_roi=target_roi,
            budget_limit=max_budget
        )
        return optimized
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/simulations/history")
async def get_simulation_history(limit: int = 10):
    """
    Get history of previous simulations
    """
    try:
        history = simulation_service.get_simulation_history(limit)
        return {"simulations": history}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))