#!/usr/bin/env python3
"""
Deploy trained model to production
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / 'backend'))

import shutil
import joblib
from datetime import datetime

def main():
    print("🔄 Model Deployment Script")
    print("="*50)
    
    # Paths
    model_dir = Path(__file__).parent.parent / 'backend' / 'data' / 'models'
    backup_dir = model_dir / 'backups'
    
    # Create backup directory
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if model exists
    model_path = model_dir / 'churn_model.pkl'
    
    if not model_path.exists():
        print("❌ No model found to deploy. Please train model first.")
        return
    
    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = backup_dir / f'churn_model_{timestamp}.pkl'
    shutil.copy(model_path, backup_path)
    print(f"✅ Backup created: {backup_path}")
    
    # Load and validate model
    model = joblib.load(model_path)
    print(f"✅ Model loaded successfully")
    print(f"   Model type: {type(model).__name__}")
    
    # Deployment info
    print("\n📋 Deployment Information:")
    print(f"   Model Path: {model_path}")
    print(f"   Backup Path: {backup_path}")
    print(f"   Deployment Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Create deployment record
    deployment_record = {
        'model_path': str(model_path),
        'backup_path': str(backup_path),
        'deployed_at': timestamp,
        'status': 'success'
    }
    
    # Save deployment record
    record_path = model_dir / 'deployment_record.txt'
    with open(record_path, 'w') as f:
        for key, value in deployment_record.items():
            f.write(f"{key}: {value}\n")
    
    print(f"\n✅ Deployment successful!")
    print(f"📄 Deployment record saved to: {record_path}")

if __name__ == "__main__":
    main()