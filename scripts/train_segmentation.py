#!/usr/bin/env python3
"""
Train Customer Segmentation Model (K-Means)
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'backend'))

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import joblib

def generate_customer_data(n_samples=2000):
    """Generate synthetic customer data for segmentation"""
    np.random.seed(42)
    
    data = {
        'customer_id': [f'CUST{i:04d}' for i in range(n_samples)],
        'tenure_months': np.random.randint(1, 72, n_samples),
        'monthly_charges': np.random.uniform(20, 120, n_samples),
        'total_charges': np.random.uniform(100, 5000, n_samples),
    }
    
    df = pd.DataFrame(data)
    return df

def main():
    print("Generating customer data for segmentation...")
    df = generate_customer_data(2000)
    
    # Prepare features
    features = ['tenure_months', 'monthly_charges', 'total_charges']
    X = df[features]
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Apply KMeans
    print("Training K-Means model...")
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    segments = kmeans.fit_predict(X_scaled)
    
    df['segment'] = segments
    
    # Analyze segments
    print("\nSegment Analysis:")
    print("-" * 40)
    segment_stats = df.groupby('segment')[features].mean().round(2)
    segment_stats['size'] = df.groupby('segment').size()
    print(segment_stats)
    
    # Save model and scaler
    model_path = Path(__file__).parent.parent / 'backend' / 'data' / 'models' / 'kmeans_model.pkl'
    scaler_path = Path(__file__).parent.parent / 'backend' / 'data' / 'models' / 'scaler.pkl'
    
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(kmeans, model_path)
    joblib.dump(scaler, scaler_path)
    
    print(f"\n✅ K-Means model saved to: {model_path}")
    print(f"✅ Scaler saved to: {scaler_path}")

if __name__ == "__main__":
    main()