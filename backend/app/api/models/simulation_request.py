from pydantic import BaseModel, Field, field_validator
from typing import List, Optional

class StrategyConfig(BaseModel):
    strategy_name: str = Field(..., min_length=1, max_length=100)
    target_segment: int = Field(..., ge=0, le=3)
    discount_percent: float = Field(0, ge=0, le=100)
    free_services: List[str] = []
    contract_upgrade_months: int = Field(0, ge=0, le=24)
    priority_support: bool = False
    cost_per_customer: float = Field(..., ge=0, le=500)

class SimulationRequest(BaseModel):
    strategy: StrategyConfig
    num_customers_to_target: int = Field(..., gt=0, le=10000)
    expected_success_rate: float = Field(..., ge=0, le=100)
    simulation_period_months: int = Field(6, ge=1, le=36)
    
    @field_validator('num_customers_to_target')
    def validate_target_size(cls, v):
        if v > 5000:
            raise ValueError('Cannot target more than 5000 customers in single simulation')
        return v