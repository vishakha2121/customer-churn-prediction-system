from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
import logging
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from app.config import settings
from app.api.routes import churn, segmentation, retention, simulation, dashboard, upload
from app.database.db_connection import engine, Base
from app.utils.helpers import setup_logging

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Customer Churn Prediction & Retention System",
    description="AI-powered customer churn prediction and retention optimization system",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Trusted host middleware
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "127.0.0.1"]
)

# Create database tables
@app.on_event("startup")
async def startup_event():
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down application")

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Customer Churn Prediction & Retention System API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }

# Health check
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Include routers
app.include_router(churn.router, prefix="/api/churn", tags=["Churn Prediction"])
app.include_router(segmentation.router, prefix="/api/segmentation", tags=["Customer Segmentation"])
app.include_router(retention.router, prefix="/api/retention", tags=["Retention Strategies"])
app.include_router(simulation.router, prefix="/api/simulation", tags=["ROI Simulation"])
app.include_router(dashboard.router, prefix="/api/dashboard", tags=["Dashboard"])
app.include_router(upload.router, prefix="/api/upload", tags=["Data Upload"])