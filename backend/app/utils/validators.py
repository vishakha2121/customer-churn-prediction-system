import re
from typing import Dict, Any, List
import pandas as pd

def validate_customer_data(data: Dict) -> Dict:
    """Validate customer data"""
    errors = []
    
    # Required fields
    required_fields = ['customer_id', 'tenure_months', 'monthly_charges', 'total_charges', 
                      'contract_type', 'payment_method']
    
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")
    
    # Validate email if present
    if 'email' in data and data['email']:
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, data['email']):
            errors.append("Invalid email format")
    
    # Validate tenure
    if 'tenure_months' in data:
        tenure = data['tenure_months']
        if not isinstance(tenure, (int, float)) or tenure < 0 or tenure > 100:
            errors.append("Tenure must be between 0 and 100 months")
    
    # Validate monthly charges
    if 'monthly_charges' in data:
        charges = data['monthly_charges']
        if not isinstance(charges, (int, float)) or charges < 0 or charges > 1000:
            errors.append("Monthly charges must be between 0 and 1000")
    
    # Validate contract type
    valid_contracts = ['Month-to-month', 'One year', 'Two year']
    if 'contract_type' in data and data['contract_type'] not in valid_contracts:
        errors.append(f"Invalid contract type. Must be one of: {valid_contracts}")
    
    # Validate payment method
    valid_payments = ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card']
    if 'payment_method' in data and data['payment_method'] not in valid_payments:
        errors.append(f"Invalid payment method. Must be one of: {valid_payments}")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors
    }

def validate_bulk_data(df: pd.DataFrame) -> Dict:
    """Validate bulk data from CSV"""
    errors = []
    
    # Check required columns
    required_columns = ['customer_id', 'tenure_months', 'monthly_charges', 'total_charges',
                       'contract_type', 'payment_method']
    
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        errors.append(f"Missing columns: {missing_columns}")
    
    # Check for empty dataframe
    if df.empty:
        errors.append("CSV file is empty")
    
    # Check for duplicate customer IDs
    if 'customer_id' in df.columns:
        duplicates = df[df.duplicated(['customer_id'])]
        if len(duplicates) > 0:
            errors.append(f"Found {len(duplicates)} duplicate customer IDs")
    
    # Validate contract types
    valid_contracts = ['Month-to-month', 'One year', 'Two year']
    if 'contract_type' in df.columns:
        invalid_contracts = df[~df['contract_type'].isin(valid_contracts)]
        if len(invalid_contracts) > 0:
            errors.append(f"Found {len(invalid_contracts)} invalid contract types")
    
    # Validate payment methods
    valid_payments = ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card']
    if 'payment_method' in df.columns:
        invalid_payments = df[~df['payment_method'].isin(valid_payments)]
        if len(invalid_payments) > 0:
            errors.append(f"Found {len(invalid_payments)} invalid payment methods")
    
    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "row_count": len(df)
    }