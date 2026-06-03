#!/usr/bin/env python3
"""
Train Churn Prediction Model
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'backend'))

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
import joblib

def generate_training_data(n_samples=2000):
    """Generate synthetic training data"""
    np.random.seed(42)
    
    data = {
        'customer_id': [f'CUST{i:04d}' for i in range(n_samples)],
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
    print("Generating training data...")
    df = generate_training_data(3000)
    
    print(f"Dataset shape: {df.shape}")
    print(f"Churn rate: {df['churn'].mean()*100:.2f}%")
    
    # Feature engineering
    feature_cols = ['tenure_months', 'monthly_charges', 'total_charges', 'paperless_billing']
    df['contract_encoded'] = df['contract_type'].astype('category').cat.codes
    df['payment_encoded'] = df['payment_method'].astype('category').cat.codes
    feature_cols.extend(['contract_encoded', 'payment_encoded'])
    
    X = df[feature_cols]
    y = df['churn']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"Training samples: {len(X_train)}")
    print(f"Test samples: {len(X_test)}")
    
    # Train model
    print("\nTraining Random Forest model...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    print("\nModel Evaluation:")
    print("-" * 40)
    print(classification_report(y_test, y_pred))
    print(f"ROC-AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")
    
    # Feature importance
    importance = dict(zip(feature_cols, model.feature_importances_))
    print("\nFeature Importance:")
    for feature, imp in sorted(importance.items(), key=lambda x: x[1], reverse=True):
        print(f"  {feature}: {imp:.4f}")
    
    # Save model
    model_path = Path(__file__).parent.parent / 'backend' / 'data' / 'models' / 'churn_model.pkl'
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    
    print(f"\n✅ Model saved to: {model_path}")

if __name__ == "__main__":
    main()