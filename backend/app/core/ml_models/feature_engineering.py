import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from typing import Tuple, List

class FeatureEngineer:
    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.numeric_features = [
            'tenure_months', 'monthly_charges', 'total_charges',
            'age', 'num_services'
        ]
        self.categorical_features = [
            'gender', 'contract_type', 'payment_method', 'internet_service',
            'online_security', 'online_backup', 'device_protection',
            'tech_support', 'streaming_tv', 'streaming_movies'
        ]
    
    def create_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create derived features"""
        df = df.copy()
        
        # Tenure-based features
        df['tenure_years'] = df['tenure_months'] / 12
        df['tenure_bins'] = pd.cut(df['tenure_months'], 
                                   bins=[0, 6, 12, 24, 48, 100],
                                   labels=['0-6', '6-12', '12-24', '24-48', '48+'])
        
        # Charges-based features
        df['avg_monthly_charges'] = df['total_charges'] / (df['tenure_months'] + 1)
        df['charges_per_service'] = df['monthly_charges'] / (df['num_services'] + 1)
        
        # Interaction features
        df['high_charges_long_tenure'] = ((df['monthly_charges'] > 70) & 
                                          (df['tenure_months'] > 24)).astype(int)
        df['low_tenure_high_charges'] = ((df['tenure_months'] < 12) & 
                                        (df['monthly_charges'] > 70)).astype(int)
        
        # Service count features
        service_cols = ['online_security', 'online_backup', 'device_protection',
                       'tech_support', 'streaming_tv', 'streaming_movies']
        
        for col in service_cols:
            df[f'has_{col}'] = (df[col] == 'Yes').astype(int)
        
        df['total_services'] = df[[f'has_{col}' for col in service_cols]].sum(axis=1)
        df['no_services'] = (df['total_services'] == 0).astype(int)
        
        # Risk indicators
        df['high_risk_payment'] = (df['payment_method'] == 'Electronic check').astype(int)
        df['monthly_risk'] = (df['contract_type'] == 'Month-to-month').astype(int)
        
        return df
    
    def encode_categorical(self, df: pd.DataFrame, fit: bool = True) -> pd.DataFrame:
        """Encode categorical variables"""
        df = df.copy()
        
        for col in self.categorical_features:
            if col in df.columns:
                if fit:
                    self.label_encoders[col] = LabelEncoder()
                    df[col + '_encoded'] = self.label_encoders[col].fit_transform(
                        df[col].astype(str)
                    )
                else:
                    df[col + '_encoded'] = self.label_encoders[col].transform(
                        df[col].astype(str)
                    )
        
        return df
    
    def scale_features(self, df: pd.DataFrame, fit: bool = True) -> pd.DataFrame:
        """Scale numeric features"""
        df = df.copy()
        
        # Select numeric columns that exist
        numeric_cols = [col for col in self.numeric_features if col in df.columns]
        
        if fit:
            df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        else:
            df[numeric_cols] = self.scaler.transform(df[numeric_cols])
        
        return df
    
    def prepare_for_model(self, df: pd.DataFrame, fit: bool = True) -> np.ndarray:
        """Complete feature preparation pipeline"""
        # Create features
        df = self.create_features(df)
        
        # Encode categorical
        df = self.encode_categorical(df, fit=fit)
        
        # Scale features
        df = self.scale_features(df, fit=fit)
        
        # Define final feature columns
        final_features = [
            'tenure_months', 'monthly_charges', 'total_charges',
            'paperless_billing', 'tenure_years', 'avg_monthly_charges',
            'high_charges_long_tenure', 'low_tenure_high_charges',
            'total_services', 'no_services', 'high_risk_payment',
            'monthly_risk'
        ]
        
        # Add encoded categorical columns
        for col in self.categorical_features:
            final_features.append(col + '_encoded')
        
        # Select only existing columns
        final_features = [col for col in final_features if col in df.columns]
        
        return df[final_features].values