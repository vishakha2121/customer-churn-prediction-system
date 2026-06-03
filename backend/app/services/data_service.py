import pandas as pd
import sqlite3
from typing import List, Dict, Any
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class DataService:
    def __init__(self):
        self.db_path = "../database/churn.db"
    
    def get_total_customers(self) -> int:
        """Get total number of customers"""
        # Mock data - in real implementation, query database
        return 7043
    
    def get_revenue_at_risk(self) -> float:
        """Calculate revenue at risk from high churn customers"""
        # Mock calculation
        high_risk_count = 1860
        avg_monthly_charges = 64.76
        return high_risk_count * avg_monthly_charges
    
    def get_retention_revenue_impact(self) -> Dict:
        """Get revenue impact of retention strategies"""
        return {
            'total_revenue_saved': 125000,
            'monthly_savings': 25000,
            'roi_ytd': 342,
            'customers_retained': 450
        }
    
    def get_recent_activities(self, limit: int = 10) -> List[Dict]:
        """Get recent system activities"""
        activities = [
            {
                'timestamp': (datetime.now() - timedelta(hours=i)).isoformat(),
                'action': 'Prediction made',
                'details': f'Customer {i} churn probability updated',
                'user': 'system'
            }
            for i in range(limit)
        ]
        return activities
    
    def bulk_insert_customers(self, df: pd.DataFrame) -> Dict:
        """Insert multiple customers into database"""
        # Mock implementation
        return {
            'inserted': len(df),
            'skipped': 0,
            'errors': []
        }
    
    def bulk_insert_strategies(self, df: pd.DataFrame) -> Dict:
        """Insert multiple strategies into database"""
        return {
            'inserted': len(df),
            'errors': []
        }
    
    def get_customer_template(self) -> Dict:
        """Get CSV template structure"""
        return {
            'columns': [
                'customer_id', 'name', 'email', 'age', 'gender',
                'tenure_months', 'monthly_charges', 'total_charges',
                'contract_type', 'payment_method', 'paperless_billing',
                'internet_service', 'online_security', 'online_backup',
                'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies'
            ],
            'sample_row': {
                'customer_id': 'CUST001',
                'tenure_months': 12,
                'monthly_charges': 65.50,
                'contract_type': 'Month-to-month',
                'payment_method': 'Electronic check'
            }
        }