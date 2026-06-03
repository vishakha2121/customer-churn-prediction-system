#!/usr/bin/env python3
"""
Generate Sample Customer Data
"""

import pandas as pd
import numpy as np
from pathlib import Path

def generate_sample_data(n_samples=1000):
    """Generate sample customer data"""
    np.random.seed(42)
    
    contract_types = ['Month-to-month', 'One year', 'Two year']
    payment_methods = ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card']
    internet_services = ['DSL', 'Fiber optic', 'No']
    yes_no = ['Yes', 'No']
    genders = ['Male', 'Female']
    
    data = []
    
    for i in range(n_samples):
        tenure = np.random.randint(1, 72)
        monthly_charges = np.random.uniform(20, 120)
        
        customer = {
            'customer_id': f'CUST{i+1:05d}',
            'name': f'Customer_{i+1}',
            'email': f'customer{i+1}@example.com',
            'age': np.random.randint(18, 80),
            'gender': np.random.choice(genders),
            'tenure_months': tenure,
            'monthly_charges': round(monthly_charges, 2),
            'total_charges': round(tenure * monthly_charges * np.random.uniform(0.9, 1.1), 2),
            'contract_type': np.random.choice(contract_types, p=[0.5, 0.3, 0.2]),
            'payment_method': np.random.choice(payment_methods),
            'paperless_billing': np.random.choice([True, False]),
            'internet_service': np.random.choice(internet_services),
            'online_security': np.random.choice(yes_no + ['No internet service']),
            'online_backup': np.random.choice(yes_no + ['No internet service']),
            'device_protection': np.random.choice(yes_no + ['No internet service']),
            'tech_support': np.random.choice(yes_no + ['No internet service']),
            'streaming_tv': np.random.choice(yes_no + ['No internet service']),
            'streaming_movies': np.random.choice(yes_no + ['No internet service']),
        }
        data.append(customer)
    
    df = pd.DataFrame(data)
    
    # Save to CSV
    output_path = Path(__file__).parent.parent / 'backend' / 'data' / 'raw' / 'sample_customers.csv'
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    
    print(f"✅ Generated {n_samples} sample customers")
    print(f"📁 Saved to: {output_path}")
    print(f"\nSample data:")
    print(df.head())
    
    return df

if __name__ == "__main__":
    generate_sample_data(1000)