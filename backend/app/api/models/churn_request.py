from pydantic import BaseModel, Field, field_validator
from typing import List, Optional
from datetime import datetime

class ChurnPredictionRequest(BaseModel):
    customer_id: str = Field(..., min_length=1, max_length=50)
    tenure_months: int = Field(..., ge=0, le=100)
    monthly_charges: float = Field(..., ge=0, le=1000)
    total_charges: float = Field(..., ge=0)
    contract_type: str = Field(..., pattern="^(Month-to-month|One year|Two year)$")
    payment_method: str = Field(..., pattern="^(Electronic check|Mailed check|Bank transfer|Credit card)$")
    paperless_billing: bool
    internet_service: str = Field(..., pattern="^(DSL|Fiber optic|No)$")
    online_security: str = Field(..., pattern="^(Yes|No|No internet service)$")
    online_backup: str = Field(..., pattern="^(Yes|No|No internet service)$")
    device_protection: str = Field(..., pattern="^(Yes|No|No internet service)$")
    tech_support: str = Field(..., pattern="^(Yes|No|No internet service)$")
    streaming_tv: str = Field(..., pattern="^(Yes|No|No internet service)$")
    streaming_movies: str = Field(..., pattern="^(Yes|No|No internet service)$")
    gender: Optional[str] = Field(None, pattern="^(Male|Female)$")
    age: Optional[int] = Field(None, ge=18, le=120)
    num_services: Optional[int] = None
    
    @field_validator('total_charges')
    def validate_total_charges(cls, v, info):
        values = info.data
        if 'monthly_charges' in values and 'tenure_months' in values:
            expected_min = values['monthly_charges'] * values['tenure_months'] * 0.5
            expected_max = values['monthly_charges'] * values['tenure_months'] * 1.5
            if v < expected_min or v > expected_max:
                raise ValueError(f'Total charges seems inconsistent with tenure and monthly charges')
        return v

class BatchPredictionRequest(BaseModel):
    customers: List[ChurnPredictionRequest]
    
    @field_validator('customers')
    def validate_batch_size(cls, v):
        if len(v) > 1000:
            raise ValueError('Batch size cannot exceed 1000 customers')
        return v