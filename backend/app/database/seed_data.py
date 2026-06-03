from app.database.db_connection import SessionLocal, engine, Base
from app.database.models import Customer, Segment, RetentionStrategy
import pandas as pd
import numpy as np
from datetime import datetime

def seed_database():
    """Seed database with initial data"""
    db = SessionLocal()
    
    try:
        # Create segments
        segments = [
            Segment(
                segment_id=0,
                segment_name="High-Risk Customers",
                segment_size=1250,
                avg_churn_rate=68.5,
                avg_tenure=8.5,
                avg_monthly_charges=85.30
            ),
            Segment(
                segment_id=1,
                segment_name="Premium Loyal",
                segment_size=2100,
                avg_churn_rate=12.3,
                avg_tenure=36.2,
                avg_monthly_charges=95.60
            ),
            Segment(
                segment_id=2,
                segment_name="Value Seekers",
                segment_size=2450,
                avg_churn_rate=28.7,
                avg_tenure=18.5,
                avg_monthly_charges=45.20
            ),
            Segment(
                segment_id=3,
                segment_name="New Customers",
                segment_size=1243,
                avg_churn_rate=42.3,
                avg_tenure=3.2,
                avg_monthly_charges=55.80
            )
        ]
        
        for segment in segments:
            existing = db.query(Segment).filter(Segment.segment_id == segment.segment_id).first()
            if not existing:
                db.add(segment)
        
        # Create retention strategies
        strategies = [
            RetentionStrategy(
                segment_id=0,
                strategy_name="Immediate Retention Offer",
                offer_type="discount",
                discount_percent=25,
                contract_upgrade=12,
                priority_support=True,
                success_rate=65,
                cost_per_customer=80
            ),
            RetentionStrategy(
                segment_id=1,
                strategy_name="Premium Rewards Program",
                offer_type="reward",
                discount_percent=15,
                contract_upgrade=6,
                priority_support=True,
                success_rate=75,
                cost_per_customer=50
            ),
            RetentionStrategy(
                segment_id=2,
                strategy_name="Value Bundle",
                offer_type="bundle",
                discount_percent=10,
                contract_upgrade=12,
                free_service_months=1,
                priority_support=False,
                success_rate=60,
                cost_per_customer=40
            ),
            RetentionStrategy(
                segment_id=3,
                strategy_name="Onboarding Support",
                offer_type="support",
                discount_percent=0,
                contract_upgrade=0,
                free_service_months=0,
                priority_support=True,
                success_rate=55,
                cost_per_customer=30
            )
        ]
        
        for strategy in strategies:
            existing = db.query(RetentionStrategy).filter(
                RetentionStrategy.strategy_name == strategy.strategy_name
            ).first()
            if not existing:
                db.add(strategy)
        
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    # Create tables
    Base.metadata.create_all(bind=engine)
    # Seed data
    seed_database()