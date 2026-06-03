from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.db_connection import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(100))
    email = Column(String(100))
    age = Column(Integer)
    gender = Column(String(10))
    tenure_months = Column(Integer, nullable=False)
    monthly_charges = Column(Float, nullable=False)
    total_charges = Column(Float, nullable=False)
    contract_type = Column(String(50), nullable=False)
    payment_method = Column(String(50), nullable=False)
    paperless_billing = Column(Boolean, nullable=False)
    internet_service = Column(String(50))
    online_security = Column(String(50))
    online_backup = Column(String(50))
    device_protection = Column(String(50))
    tech_support = Column(String(50))
    streaming_tv = Column(String(50))
    streaming_movies = Column(String(50))
    churn_risk_score = Column(Float, default=0.0)
    segment_id = Column(Integer, ForeignKey("segments.segment_id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    predictions = relationship("Prediction", back_populates="customer")

class Prediction(Base):
    __tablename__ = "predictions"
    
    prediction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    churn_probability = Column(Float, nullable=False)
    predicted_churn_date = Column(DateTime)
    confidence_score = Column(Float)
    model_version = Column(String(50))
    prediction_date = Column(DateTime(timezone=True), server_default=func.now())
    is_accurate = Column(Boolean, default=None)
    
    # Relationships
    customer = relationship("Customer", back_populates="predictions")

class Segment(Base):
    __tablename__ = "segments"
    
    segment_id = Column(Integer, primary_key=True, index=True)
    segment_name = Column(String(100), nullable=False)
    cluster_center_features = Column(Text)  # JSON string
    segment_size = Column(Integer)
    avg_churn_rate = Column(Float)
    avg_tenure = Column(Float)
    avg_monthly_charges = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    strategies = relationship("RetentionStrategy", back_populates="segment")

class RetentionStrategy(Base):
    __tablename__ = "retention_strategies"
    
    strategy_id = Column(Integer, primary_key=True, index=True)
    segment_id = Column(Integer, ForeignKey("segments.segment_id"))
    strategy_name = Column(String(200), nullable=False)
    offer_type = Column(String(50))
    discount_percent = Column(Float, default=0)
    contract_upgrade = Column(Integer, default=0)
    free_service_months = Column(Integer, default=0)
    priority_support = Column(Boolean, default=False)
    success_rate = Column(Float)
    cost_per_customer = Column(Float)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    segment = relationship("Segment", back_populates="strategies")
    simulations = relationship("Simulation", back_populates="strategy")

class Simulation(Base):
    __tablename__ = "simulations"
    
    simulation_id = Column(Integer, primary_key=True, index=True)
    strategy_id = Column(Integer, ForeignKey("retention_strategies.strategy_id"))
    target_segment_id = Column(Integer)
    expected_roi = Column(Float)
    estimated_savings = Column(Float)
    implementation_cost = Column(Float)
    breakeven_months = Column(Float)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    strategy = relationship("RetentionStrategy", back_populates="simulations")

class ROIMetric(Base):
    __tablename__ = "roi_metrics"
    
    metric_id = Column(Integer, primary_key=True, index=True)
    simulation_id = Column(Integer, ForeignKey("simulations.simulation_id"))
    total_customers_saved = Column(Integer)
    revenue_saved = Column(Float)
    cost_incurred = Column(Float)
    net_savings = Column(Float)
    roi_percentage = Column(Float)
    payback_period = Column(Float)
    calculated_at = Column(DateTime(timezone=True), server_default=func.now())