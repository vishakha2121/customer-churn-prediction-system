import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class KMeansSegmenter:
    def __init__(self, n_segments=4, random_state=42):
        self.n_segments = n_segments
        self.random_state = random_state
        self.kmeans = KMeans(n_clusters=n_segments, random_state=random_state, n_init=10)
        self.scaler = StandardScaler()
    
    def prepare_features(self, df):
        """Prepare features for segmentation"""
        features = pd.DataFrame()
        
        # Behavioral features
        features['tenure_months'] = df['tenure_months']
        features['monthly_charges'] = df['monthly_charges']
        features['total_charges'] = df['total_charges']
        
        # Service usage
        service_cols = ['online_security', 'online_backup', 'device_protection',
                       'tech_support', 'streaming_tv', 'streaming_movies']
        
        for col in service_cols:
            features[f'has_{col}'] = (df[col] == 'Yes').astype(int)
        
        features['total_services'] = features[[f'has_{col}' for col in service_cols]].sum(axis=1)
        
        # Payment and contract
        features['month_to_month'] = (df['contract_type'] == 'Month-to-month').astype(int)
        features['electronic_check'] = (df['payment_method'] == 'Electronic check').astype(int)
        features['paperless'] = df['paperless_billing'].astype(int)
        
        # Risk indicators
        features['high_risk'] = ((features['month_to_month'] == 1) & 
                                (features['electronic_check'] == 1)).astype(int)
        
        return features
    
    def fit(self, df):
        """Fit KMeans on customer data"""
        features = self.prepare_features(df)
        
        # Scale features
        scaled_features = self.scaler.fit_transform(features)
        
        # Fit KMeans
        self.kmeans.fit(scaled_features)
        
        # Add segment labels
        df['segment'] = self.kmeans.labels_
        
        # Analyze segments
        segment_profiles = self._analyze_segments(df)
        
        return df, segment_profiles
    
    def predict(self, df):
        """Assign segments to new customers"""
        features = self.prepare_features(df)
        scaled_features = self.scaler.transform(features)
        segments = self.kmeans.predict(scaled_features)
        
        return segments
    
    def _analyze_segments(self, df):
        """Analyze and profile each segment"""
        profiles = []
        
        for segment_id in range(self.n_segments):
            segment_data = df[df['segment'] == segment_id]
            
            profile = {
                'segment_id': int(segment_id),
                'size': len(segment_data),
                'percentage': (len(segment_data) / len(df)) * 100,
                'avg_tenure': segment_data['tenure_months'].mean(),
                'avg_monthly_charges': segment_data['monthly_charges'].mean(),
                'avg_total_services': segment_data[['online_security', 'online_backup']].apply(
                    lambda x: (x == 'Yes').sum(), axis=1
                ).mean() if 'online_security' in segment_data else 0,
                'month_to_month_pct': (segment_data['contract_type'] == 'Month-to-month').mean() * 100,
                'electronic_check_pct': (segment_data['payment_method'] == 'Electronic check').mean() * 100,
                'avg_churn_risk': segment_data.get('churn_risk_score', 0.5).mean()
            }
            
            # Segment name based on characteristics
            if profile['avg_tenure'] < 6:
                profile['segment_name'] = 'New Customers'
            elif profile['avg_monthly_charges'] > 70:
                if profile['month_to_month_pct'] > 50:
                    profile['segment_name'] = 'High-Value At-Risk'
                else:
                    profile['segment_name'] = 'Premium Loyal'
            elif profile['avg_tenure'] > 24:
                profile['segment_name'] = 'Long-Term Loyal'
            else:
                profile['segment_name'] = 'Regular Customers'
            
            profiles.append(profile)
        
        return profiles
    
    def save_model(self, model_path):
        """Save KMeans model and scaler"""
        Path(model_path).parent.mkdir(parents=True, exist_ok=True)
        joblib.dump({
            'kmeans': self.kmeans,
            'scaler': self.scaler
        }, model_path)
        logger.info(f"Segmentation model saved to {model_path}")
    
    def load_model(self, model_path):
        """Load KMeans model and scaler"""
        data = joblib.load(model_path)
        self.kmeans = data['kmeans']
        self.scaler = data['scaler']
        self.n_segments = self.kmeans.n_clusters
        logger.info(f"Segmentation model loaded from {model_path}")