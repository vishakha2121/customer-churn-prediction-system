import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

class Settings:
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///../database/churn.db")
    
    # API Keys
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # Model paths
    MODEL_PATH: str = os.getenv("MODEL_PATH", "./data/models/churn_model.pkl")
    SCALER_PATH: str = os.getenv("SCALER_PATH", "./data/models/scaler.pkl")
    KMEANS_PATH: str = os.getenv("KMEANS_PATH", "./data/models/kmeans_model.pkl")
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-this")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # App settings
    APP_NAME: str = "Customer Churn Prediction System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # ML Settings
    RANDOM_STATE: int = 42
    TEST_SIZE: float = 0.2
    CHURN_THRESHOLD: float = 0.5

settings = Settings()