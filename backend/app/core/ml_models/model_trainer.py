import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

class ModelTrainer:
    def __init__(self):
        self.models = {
            'random_forest': RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42
            ),
            'gradient_boosting': GradientBoostingClassifier(
                n_estimators=100,
                learning_rate=0.1,
                random_state=42
            ),
            'logistic_regression': LogisticRegression(
                max_iter=1000,
                random_state=42
            )
        }
        self.best_model = None
        self.best_model_name = None
    
    def train_models(self, X_train, y_train, X_val, y_val):
        """Train multiple models and select best"""
        results = {}
        
        for name, model in self.models.items():
            logger.info(f"Training {name}...")
            
            # Train model
            model.fit(X_train, y_train)
            
            # Predict on validation
            y_pred = model.predict(X_val)
            y_pred_proba = model.predict_proba(X_val)[:, 1]
            
            # Calculate metrics
            metrics = {
                'accuracy': accuracy_score(y_val, y_pred),
                'precision': precision_score(y_val, y_pred),
                'recall': recall_score(y_val, y_pred),
                'f1': f1_score(y_val, y_pred),
                'roc_auc': roc_auc_score(y_val, y_pred_proba)
            }
            
            results[name] = {
                'model': model,
                'metrics': metrics
            }
            
            logger.info(f"{name} - F1: {metrics['f1']:.3f}, AUC: {metrics['roc_auc']:.3f}")
        
        # Select best model (based on F1 score)
        best_f1 = 0
        for name, result in results.items():
            if result['metrics']['f1'] > best_f1:
                best_f1 = result['metrics']['f1']
                self.best_model = result['model']
                self.best_model_name = name
        
        logger.info(f"Best model: {self.best_model_name} with F1: {best_f1:.3f}")
        
        return results
    
    def cross_validate(self, X, y, cv=5):
        """Perform cross-validation on best model"""
        if self.best_model is None:
            raise ValueError("No model trained yet")
        
        scores = cross_val_score(
            self.best_model, X, y, 
            cv=cv, scoring='f1'
        )
        
        logger.info(f"Cross-validation F1 scores: {scores}")
        logger.info(f"Mean F1: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")
        
        return {
            'scores': scores.tolist(),
            'mean': scores.mean(),
            'std': scores.std()
        }
    
    def save_model(self, model_path, scaler=None):
        """Save trained model to disk"""
        if self.best_model is None:
            raise ValueError("No model to save")
        
        # Save model
        Path(model_path).parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.best_model, model_path)
        logger.info(f"Model saved to {model_path}")
        
        # Save scaler if provided
        if scaler:
            scaler_path = model_path.replace('churn_model.pkl', 'scaler.pkl')
            joblib.dump(scaler, scaler_path)
            logger.info(f"Scaler saved to {scaler_path}")
    
    def get_feature_importance(self, feature_names):
        """Get feature importance from best model"""
        if self.best_model is None:
            raise ValueError("No model trained yet")
        
        if hasattr(self.best_model, 'feature_importances_'):
            importance = self.best_model.feature_importances_
            return dict(zip(feature_names, importance))
        elif hasattr(self.best_model, 'coef_'):
            importance = np.abs(self.best_model.coef_[0])
            return dict(zip(feature_names, importance))
        else:
            return None