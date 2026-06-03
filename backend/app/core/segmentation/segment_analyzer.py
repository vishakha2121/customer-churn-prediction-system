import pandas as pd
import numpy as np
from typing import Dict, List, Any

class SegmentAnalyzer:
    def __init__(self):
        self.segment_profiles = {}
    
    def analyze_segment(self, segment_data: pd.DataFrame, segment_id: int) -> Dict[str, Any]:
        """Comprehensive analysis of a single segment"""
        analysis = {
            'segment_id': segment_id,
            'size': len(segment_data),
            'basic_stats': {
                'avg_tenure': segment_data['tenure_months'].mean(),
                'median_tenure': segment_data['tenure_months'].median(),
                'avg_monthly_charges': segment_data['monthly_charges'].mean(),
                'avg_total_charges': segment_data['total_charges'].mean(),
            },
            'churn_metrics': {
                'avg_churn_risk': segment_data.get('churn_risk_score', 0.5).mean(),
                'high_risk_count': (segment_data.get('churn_risk_score', 0.5) > 0.7).sum(),
            },
            'demographics': {
                'gender_distribution': segment_data['gender'].value_counts().to_dict() if 'gender' in segment_data else {},
                'avg_age': segment_data['age'].mean() if 'age' in segment_data else 0,
            },
            'service_usage': {
                'avg_services': sum([
                    (segment_data[col] == 'Yes').sum() 
                    for col in ['online_security', 'online_backup', 'device_protection',
                               'tech_support', 'streaming_tv', 'streaming_movies']
                ]) / len(segment_data) if len(segment_data) > 0 else 0,
            },
            'contract_distribution': segment_data['contract_type'].value_counts().to_dict(),
            'payment_distribution': segment_data['payment_method'].value_counts().to_dict(),
        }
        
        # Add segment insights
        analysis['insights'] = self._generate_insights(analysis)
        
        return analysis
    
    def _generate_insights(self, analysis: Dict) -> List[str]:
        """Generate actionable insights for a segment"""
        insights = []
        
        # Tenure insights
        if analysis['basic_stats']['avg_tenure'] < 6:
            insights.append("New customers - focus on onboarding and early engagement")
        elif analysis['basic_stats']['avg_tenure'] > 24:
            insights.append("Loyal customers - reward loyalty to maintain retention")
        
        # Churn insights
        if analysis['churn_metrics']['avg_churn_risk'] > 0.6:
            insights.append("High churn risk segment - immediate intervention needed")
        
        # Payment insights
        if analysis['payment_distribution'].get('Electronic check', 0) > 0.5:
            insights.append("High electronic check usage - consider incentives for auto-pay")
        
        # Contract insights
        if analysis['contract_distribution'].get('Month-to-month', 0) > 0.5:
            insights.append("Majority on month-to-month - offer contract incentives")
        
        # Service insights
        if analysis['service_usage']['avg_services'] < 2:
            insights.append("Low service adoption - bundle promotions could increase stickiness")
        
        return insights
    
    def compare_segments(self, segment1_data: pd.DataFrame, segment2_data: pd.DataFrame) -> Dict:
        """Compare two segments"""
        comparison = {
            'size_ratio': len(segment1_data) / len(segment2_data),
            'tenure_difference': segment1_data['tenure_months'].mean() - segment2_data['tenure_months'].mean(),
            'charges_difference': segment1_data['monthly_charges'].mean() - segment2_data['monthly_charges'].mean(),
            'churn_risk_difference': segment1_data.get('churn_risk_score', 0.5).mean() - 
                                     segment2_data.get('churn_risk_score', 0.5).mean(),
        }
        
        return comparison