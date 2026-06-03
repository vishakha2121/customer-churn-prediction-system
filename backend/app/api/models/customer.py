from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime

class CustomerBase(BaseModel):
    customer_id: str = Field(..., min_length=1, max_length=50)
    name: Optional[str] = None
    email: Optional[str] = Field(None, pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    age: Optional[int] = Field(None, ge=18, le=120)
    gender: Optional[str] = Field(None, pattern="^(Male|Female)$")
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
    
    @field_validator('email')
    def validate_email(cls, v):
        if v is not None:
            import re
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
                raise ValueError('Invalid email format')
        return v

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    monthly_charges: Optional[float] = Field(None, ge=0, le=1000)
    contract_type: Optional[str] = Field(None, pattern="^(Month-to-month|One year|Two year)$")
    payment_method: Optional[str] = Field(None, pattern="^(Electronic check|Mailed check|Bank transfer|Credit card)$")

class CustomerResponse(CustomerBase):
    id: int
    churn_risk_score: Optional[float] = None
    segment_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True