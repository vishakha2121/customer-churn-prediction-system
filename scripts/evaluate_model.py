#!/usr/bin/env python3
"""
Evaluate Churn Prediction Model
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'backend'))

import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

def generate_test_data(n_samples=500):
    """Generate test data"""
    np.random.seed(123)
    
    data = {
        'customer_id': [f'TEST{i:04d}' for i in range(n_samples)],
        'tenure_months': np.random.randint(1, 72, n_samples),
        'monthly_charges': np.random.uniform(20, 120, n_samples),
        'total_charges': np.random.uniform(100, 5000, n_samples),
        'contract_type': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples),
        'payment_method': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], n_samples),
        'paperless_billing': np.random.choice([0, 1], n_samples),
    }
    
    df = pd.DataFrame(data)
    
    # Generate churn labels
    churn_prob = []
    for i in range(n_samples):
        prob = 0.2
        if df.loc[i, 'contract_type'] == 'Month-to-month':
            prob += 0.3
        if df.loc[i, 'tenure_months'] < 12:
            prob += 0.2
        if df.loc[i, 'monthly_charges'] > 70:
            prob += 0.2
        churn_prob.append(min(prob, 0.95))
    
    df['churn'] = (np.random.random(n_samples) < churn_prob).astype(int)
    
    return df

def main():
    print("Loading model...")
    model_path = Path(__file__).parent.parent / 'backend' / 'data' / 'models' / 'churn_model.pkl'
    
    if not model_path.exists():
        print("❌ Model not found. Please run train_churn_model.py first")
        return
    
    model = joblib.load(model_path)
    print("✅ Model loaded successfully")
    
    print("\nGenerating test data...")
    df = generate_test_data(500)
    
    # Prepare features
    feature_cols = ['tenure_months', 'monthly_charges', 'total_charges', 'paperless_billing']
    df['contract_encoded'] = df['contract_type'].astype('category').cat.codes
    df['payment_encoded'] = df['payment_method'].astype('category').cat.codes
    feature_cols.extend(['contract_encoded', 'payment_encoded'])
    
    X = df[feature_cols]
    y = df['churn']
    
    print(f"Test samples: {len(X)}")
    
    # Predict
    y_pred = model.predict(X)
    y_pred_proba = model.predict_proba(X)[:, 1]
    
    print("\n" + "="*50)
    print("MODEL EVALUATION REPORT")
    print("="*50)
    
    print("\nClassification Report:")
    print("-"*40)
    print(classification_report(y, y_pred, target_names=['Not Churn', 'Churn']))
    
    print("\nConfusion Matrix:")
    print("-"*40)
    print(confusion_matrix(y, y_pred))
    
    print(f"\nROC-AUC Score: {roc_auc_score(y, y_pred_proba):.4f}")
    
    # Calculate accuracy
    accuracy = (y_pred == y).mean()
    print(f"\nOverall Accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    main()