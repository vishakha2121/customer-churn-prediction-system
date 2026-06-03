from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np
from app.core.segmentation.kmeans_segmenter import KMeansSegmenter

class SegmentationService:
    def __init__(self):
        self.segmenter = KMeansSegmenter(n_segments=4)
        self.segments_data = self._initialize_segments()
    
    def _initialize_segments(self):
        """Initialize segment profiles"""
        return [
            {
                'segment_id': 0,
                'segment_name': 'High-Risk Customers',
                'size': 1250,
                'avg_tenure': 8.5,
                'avg_monthly_charges': 85.30,
                'avg_churn_rate': 68.5,
                'characteristics': 'Short tenure, high monthly charges, month-to-month contracts'
            },
            {
                'segment_id': 1,
                'segment_name': 'Premium Loyal',
                'size': 2100,
                'avg_tenure': 36.2,
                'avg_monthly_charges': 95.60,
                'avg_churn_rate': 12.3,
                'characteristics': 'Long tenure, high value, multiple services'
            },
            {
                'segment_id': 2,
                'segment_name': 'Value Seekers',
                'size': 2450,
                'avg_tenure': 18.5,
                'avg_monthly_charges': 45.20,
                'avg_churn_rate': 28.7,
                'characteristics': 'Moderate tenure, low charges, basic services'
            },
            {
                'segment_id': 3,
                'segment_name': 'New Customers',
                'size': 1243,
                'avg_tenure': 3.2,
                'avg_monthly_charges': 55.80,
                'avg_churn_rate': 42.3,
                'characteristics': 'New customers, exploring services'
            }
        ]
    
    def get_segments_summary(self) -> List[Dict]:
        """Get summary of all segments"""
        return self.segments_data
    
    def get_segment_by_id(self, segment_id: int) -> Optional[Dict]:
        """Get segment by ID"""
        for segment in self.segments_data:
            if segment['segment_id'] == segment_id:
                return segment
        return None
    
    def assign_customer_to_segment(self, customer_id: str) -> Dict:
        """Assign customer to appropriate segment (mock implementation)"""
        # In real implementation, use KMeans to assign
        segment_id = hash(customer_id) % 4
        segment = self.get_segment_by_id(segment_id)
        
        return {
            'segment_id': segment_id,
            'segment_name': segment['segment_name'],
            'avg_churn_rate': segment['avg_churn_rate']
        }
    
    def get_segment_distribution(self) -> Dict:
        """Get distribution of customers across segments"""
        total = sum(s['size'] for s in self.segments_data)
        
        return {
            'segments': [
                {
                    'segment_id': s['segment_id'],
                    'segment_name': s['segment_name'],
                    'count': s['size'],
                    'percentage': round((s['size'] / total) * 100, 2)
                }
                for s in self.segments_data
            ],
            'total_customers': total
        }
    
    def get_segment_characteristics(self, segment_id: int) -> Dict:
        """Get detailed characteristics of a segment"""
        segment = self.get_segment_by_id(segment_id)
        
        if not segment:
            return {}
        
        return {
            'demographics': {
                'age_distribution': {
                    '18-30': 25,
                    '31-45': 40,
                    '46-60': 25,
                    '60+': 10
                },
                'gender_ratio': {'Male': 48, 'Female': 52}
            },
            'behavioral': {
                'avg_monthly_usage': 150,
                'avg_support_tickets': 1.2,
                'service_adoption_rate': 65
            },
            'financial': {
                'avg_clv': 2500,
                'payment_behavior': 'On time'
            }
        }
    
    def get_segment_performance(self) -> List[Dict]:
        """Get performance metrics by segment"""
        return [
            {
                'segment_id': s['segment_id'],
                'segment_name': s['segment_name'],
                'revenue_contribution': round(s['size'] * s['avg_monthly_charges'], 2),
                'churn_impact': round((s['avg_churn_rate'] / 100) * s['size'] * s['avg_monthly_charges'] * 12, 2),
                'retention_priority': 'High' if s['avg_churn_rate'] > 40 else 'Medium' if s['avg_churn_rate'] > 20 else 'Low'
            }
            for s in self.segments_data
        ]