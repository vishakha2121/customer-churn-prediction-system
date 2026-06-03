from typing import Dict, List, Any
from datetime import datetime
import numpy as np
from app.core.ml_models.churn_predictor import ChurnPredictor

class PredictionService:
    def __init__(self):
        self.predictor = ChurnPredictor()
    
    def predict_single(self, customer_data: Dict) -> Dict:
        """Predict churn for single customer"""
        probability = self.predictor.predict(customer_data)[0]
        
        # Determine risk level
        if probability >= 0.7:
            risk_level = "High"
        elif probability >= 0.4:
            risk_level = "Medium"
        else:
            risk_level = "Low"
        
        return {
            "probability": float(probability),
            "risk_level": risk_level,
            "timestamp": datetime.now().isoformat(),
            "confidence": 0.85 if probability > 0.1 and probability < 0.9 else 0.95
        }
    
    def predict_batch(self, customers: List[Dict]) -> List[Dict]:
        """Predict churn for multiple customers"""
        predictions = []
        
        for customer in customers:
            pred = self.predict_single(customer)
            pred["customer_id"] = customer.get("customer_id")
            predictions.append(pred)
        
        return predictions
    
    def get_average_churn_rate(self) -> float:
        """Get average churn rate across all customers"""
        # Mock data - in real implementation calculate from predictions
        return 26.5
    
    def get_high_risk_count(self) -> int:
        """Get number of high-risk customers"""
        return 1860
    
    def get_churn_trend(self, days: int = 30) -> List[Dict]:
        """Get churn rate trend over time"""
        # Generate mock trend data
        trend = []
        base_rate = 25
        
        for i in range(days):
            date = (datetime.now() - datetime.timedelta(days=days-i-1)).date()
            churn_rate = base_rate + np.random.normal(0, 2)
            trend.append({
                'date': date.isoformat(),
                'churn_rate': round(max(0, min(100, churn_rate)), 2)
            })
        
        return trend
    
    def get_prediction_distribution(self) -> Dict:
        """Get distribution of churn predictions"""
        return {
            'high_risk': 26.4,
            'medium_risk': 45.2,
            'low_risk': 28.4
        }
    
    def get_model_metrics(self) -> Dict:
        """Get model performance metrics"""
        return {
            'accuracy': 0.85,
            'precision': 0.82,
            'recall': 0.79,
            'f1_score': 0.80,
            'roc_auc': 0.88,
            'last_trained': '2024-01-15'
        }
    
    def get_feature_importance(self) -> List[Dict]:
        """Get feature importance scores"""
        return [
            {'feature': 'tenure_months', 'importance': 0.25},
            {'feature': 'contract_type', 'importance': 0.20},
            {'feature': 'monthly_charges', 'importance': 0.15},
            {'feature': 'total_services', 'importance': 0.12},
            {'feature': 'payment_method', 'importance': 0.10}
        ]