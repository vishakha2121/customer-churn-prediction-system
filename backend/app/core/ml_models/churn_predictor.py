import joblib
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class ChurnPredictor:
    def __init__(self, model_path=None, scaler_path=None):
        self.model_path = model_path or "./data/models/churn_model.pkl"
        self.scaler_path = scaler_path or "./data/models/scaler.pkl"
        self.model = None
        self.scaler = None
        self.load_models()
    
    def load_models(self):
        """Load trained models from disk"""
        try:
            if Path(self.model_path).exists():
                self.model = joblib.load(self.model_path)
                logger.info(f"Model loaded from {self.model_path}")
            else:
                logger.warning(f"Model not found at {self.model_path}")
                self.model = None
            
            if Path(self.scaler_path).exists():
                self.scaler = joblib.load(self.scaler_path)
                logger.info(f"Scaler loaded from {self.scaler_path}")
            else:
                logger.warning(f"Scaler not found at {self.scaler_path}")
                self.scaler = None
        except Exception as e:
            logger.error(f"Error loading models: {e}")
            self.model = None
            self.scaler = None
    
    def predict(self, features):
        """Predict churn probability"""
        if self.model is None:
            # Return mock predictions if model not trained
            return self._mock_predict(features)
        
        try:
            # Preprocess features
            processed_features = self._preprocess_features(features)
            
            # Scale features if scaler exists
            if self.scaler is not None:
                processed_features = self.scaler.transform(processed_features)
            
            # Predict probability
            probability = self.model.predict_proba(processed_features)[:, 1]
            
            return probability
        except Exception as e:
            logger.error(f"Prediction error: {e}")
            return self._mock_predict(features)
    
    def _preprocess_features(self, features):
        """Convert raw features to model input format"""
        # This should match your training feature engineering
        df = pd.DataFrame([features])
        
        # Create derived features
        df['avg_monthly_charges'] = df['total_charges'] / (df['tenure_months'] + 1)
        df['tenure_years'] = df['tenure_months'] / 12
        df['high_charges'] = (df['monthly_charges'] > 70).astype(int)
        df['long_tenure'] = (df['tenure_months'] > 24).astype(int)
        
        # Encode categorical variables
        categorical_cols = ['contract_type', 'payment_method', 'internet_service',
                           'online_security', 'online_backup', 'device_protection',
                           'tech_support', 'streaming_tv', 'streaming_movies']
        
        for col in categorical_cols:
            if col in df.columns:
                df[col + '_encoded'] = df[col].astype('category').cat.codes
        
        # Select features for model (adjust based on your trained model)
        feature_cols = ['tenure_months', 'monthly_charges', 'total_charges',
                       'paperless_billing', 'avg_monthly_charges', 'tenure_years',
                       'high_charges', 'long_tenure']
        
        # Add encoded categorical columns
        for col in categorical_cols:
            if col + '_encoded' in df.columns:
                feature_cols.append(col + '_encoded')
        
        return df[feature_cols].values
    
    def _mock_predict(self, features):
        """Mock predictions when model is not available"""
        # Simple heuristic for demo
        risk_score = 0
        if features.get('contract_type') == 'Month-to-month':
            risk_score += 0.3
        if features.get('tenure_months', 0) < 12:
            risk_score += 0.2
        if features.get('monthly_charges', 0) > 70:
            risk_score += 0.2
        if features.get('payment_method') == 'Electronic check':
            risk_score += 0.15
        if features.get('online_security') == 'No':
            risk_score += 0.15
        
        return np.array([min(risk_score, 0.95)])
    
    def get_feature_importance(self):
        """Get feature importance scores"""
        if self.model and hasattr(self.model, 'feature_importances_'):
            return self.model.feature_importances_.tolist()
        return None