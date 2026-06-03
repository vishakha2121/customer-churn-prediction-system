from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import pandas as pd
import io

from app.services.data_service import DataService
from app.utils.validators import validate_bulk_data

router = APIRouter()
data_service = DataService()

@router.post("/customers/csv")
async def upload_customers_csv(file: UploadFile = File(...)):
    """
    Upload customer data from CSV file
    """
    try:
        # Check file type
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        # Read CSV
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        
        # Validate data
        validation = validate_bulk_data(df)
        if not validation["valid"]:
            raise HTTPException(status_code=400, detail=validation["errors"])
        
        # Save to database
        result = data_service.bulk_insert_customers(df)
        
        return {
            "message": f"Successfully uploaded {result['inserted']} customers",
            "total_rows": len(df),
            "inserted": result["inserted"],
            "skipped": result["skipped"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/strategies/bulk")
async def upload_strategies_csv(file: UploadFile = File(...)):
    """
    Upload retention strategies from CSV
    """
    try:
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Only CSV files are allowed")
        
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode('utf-8')))
        
        result = data_service.bulk_insert_strategies(df)
        
        return {
            "message": f"Successfully uploaded {result['inserted']} strategies",
            "total_rows": len(df),
            "inserted": result["inserted"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/template/customers")
async def download_customer_template():
    """
    Download template for customer data upload
    """
    try:
        template = data_service.get_customer_template()
        return template
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))