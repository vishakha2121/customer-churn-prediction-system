from sqlalchemy.orm import Session
from app.database.db_connection import SessionLocal
from app.database.models import Customer, Prediction, Segment, RetentionStrategy, Simulation, ROIMetric
from typing import Dict, List, Optional
from datetime import datetime

class CRUDOperations:
    def __init__(self):
        self.db = SessionLocal()
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """Get customer by ID"""
        return self.db.query(Customer).filter(Customer.customer_id == customer_id).first()
    
    def get_all_customers(self, skip: int = 0, limit: int = 100) -> List[Customer]:
        """Get all customers with pagination"""
        return self.db.query(Customer).offset(skip).limit(limit).all()
    
    def create_customer(self, customer_data: Dict) -> Customer:
        """Create new customer"""
        customer = Customer(**customer_data)
        self.db.add(customer)
        self.db.commit()
        self.db.refresh(customer)
        return customer
    
    def update_customer(self, customer_id: str, update_data: Dict) -> Optional[Customer]:
        """Update customer information"""
        customer = self.get_customer(customer_id)
        if customer:
            for key, value in update_data.items():
                setattr(customer, key, value)
            self.db.commit()
            self.db.refresh(customer)
        return customer
    
    def save_prediction(self, customer_data: Dict, prediction: Dict) -> Prediction:
        """Save churn prediction"""
        # Get customer by ID
        customer = self.get_customer(customer_data.get('customer_id'))
        if not customer:
            # Create new customer if doesn't exist (for demo)
            customer = self.create_customer({
                'customer_id': customer_data.get('customer_id'),
                'tenure_months': customer_data.get('tenure_months', 0),
                'monthly_charges': customer_data.get('monthly_charges', 0),
                'total_charges': customer_data.get('total_charges', 0),
                'contract_type': customer_data.get('contract_type', 'Month-to-month'),
                'payment_method': customer_data.get('payment_method', 'Electronic check'),
                'paperless_billing': customer_data.get('paperless_billing', False),
                'internet_service': customer_data.get('internet_service', 'No'),
                'online_security': customer_data.get('online_security', 'No'),
                'online_backup': customer_data.get('online_backup', 'No'),
                'device_protection': customer_data.get('device_protection', 'No'),
                'tech_support': customer_data.get('tech_support', 'No'),
                'streaming_tv': customer_data.get('streaming_tv', 'No'),
                'streaming_movies': customer_data.get('streaming_movies', 'No')
            })
        
        prediction_record = Prediction(
            customer_id=customer.id,
            churn_probability=prediction['probability'] * 100,
            confidence_score=prediction.get('confidence', 0.85) * 100,
            model_version="1.0.0",
            prediction_date=datetime.now()
        )
        self.db.add(prediction_record)
        self.db.commit()
        self.db.refresh(prediction_record)
        
        # Update customer churn risk score
        customer.churn_risk_score = prediction['probability'] * 100
        self.db.commit()
        
        return prediction_record
    
    def get_segment(self, segment_id: int) -> Optional[Segment]:
        """Get segment by ID"""
        return self.db.query(Segment).filter(Segment.segment_id == segment_id).first()
    
    def get_all_segments(self) -> List[Segment]:
        """Get all segments"""
        return self.db.query(Segment).all()
    
    def create_strategy(self, strategy_data: Dict) -> RetentionStrategy:
        """Create retention strategy"""
        strategy = RetentionStrategy(**strategy_data)
        self.db.add(strategy)
        self.db.commit()
        self.db.refresh(strategy)
        return strategy
    
    def get_strategies_for_segment(self, segment_id: int) -> List[RetentionStrategy]:
        """Get strategies for a specific segment"""
        return self.db.query(RetentionStrategy).filter(RetentionStrategy.segment_id == segment_id).all()
    
    def create_simulation(self, simulation_data: Dict) -> Simulation:
        """Create simulation record"""
        simulation = Simulation(**simulation_data)
        self.db.add(simulation)
        self.db.commit()
        self.db.refresh(simulation)
        return simulation
    
    def close(self):
        """Close database connection"""
        self.db.close()