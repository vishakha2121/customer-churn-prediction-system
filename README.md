# 🎯 Customer Churn Prediction & Retention Optimization System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18-blue.svg)](https://reactjs.org)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

## 📋 Table of Contents
- [🚀 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [📊 Model Performance](#-model-performance)
- [🛠️ Tech Stack](#️-tech-stack)
- [📁 Project Structure](#-project-structure)
- [🚀 Quick Start](#-quick-start)
- [📡 API Documentation](#-api-documentation)
- [🎨 Frontend Guide](#-frontend-guide)
- [🐳 Docker Deployment](#-docker-deployment)
- [📈 Business Impact](#-business-impact)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

## 🚀 Overview

An end-to-end **AI-powered Customer Churn Prediction System** that helps businesses identify customers at risk of churning and provides personalized retention strategies. The system achieves **85% accuracy** using Random Forest algorithm and segments customers using **K-Means clustering**.

### 🎯 Problem Statement
Customer churn is a critical challenge for subscription-based businesses. This system helps:
- **Predict** which customers are likely to churn
- **Understand** why customers churn
- **Prevent** churn with targeted retention strategies
- **Measure** ROI of retention campaigns

## ✨ Key Features

### 🔮 Churn Prediction
- Single customer prediction with 85% accuracy
- Batch prediction for multiple customers
- Real-time risk assessment
- Feature importance analysis

### 📊 Customer Segmentation
- K-Means clustering (4 segments)
- Segment-wise churn analysis
- Behavioral pattern identification
- Targeted marketing recommendations

### 💎 Retention Strategies
- AI-powered personalized offers
- Segment-specific strategies
- Discount and loyalty programs
- Priority support allocation

### 📈 ROI Simulation
- What-if scenario analysis
- Investment optimization
- Breakeven calculation
- Strategy comparison

### 🎨 Interactive Dashboard
- Real-time KPIs and metrics
- Churn trend visualization
- Segment distribution charts
- Strategy performance tracking

## 📊 Model Performance

| Metric | Score | Description |
|--------|-------|-------------|
| **Accuracy** | 85.7% | Overall prediction correctness |
| **Precision** | 82.3% | Correct positive predictions |
| **Recall** | 79.8% | Actual churners identified |
| **F1 Score** | 81.0% | Harmonic mean of precision & recall |
| **ROC-AUC** | 0.88 | Model discrimination ability |

### Feature Importance

## 🛠️ Tech Stack

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| FastAPI | 0.104.1 | REST API framework |
| scikit-learn | 1.3.2 | Machine learning |
| Pandas | 2.1.3 | Data processing |
| NumPy | 1.24.3 | Numerical computing |
| SQLAlchemy | 2.0.23 | ORM & database |
| Pydantic | 2.5.0 | Data validation |
| Uvicorn | 0.24.0 | ASGI server |
| Google Gemini AI | 0.3.2 | Strategy generation |

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18.2.0 | UI framework |
| Tailwind CSS | 3.3.6 | Styling |
| Recharts | 2.10.3 | Charts & graphs |
| Axios | 1.6.2 | API calls |
| Framer Motion | 10.16.16 | Animations |
| React Router | 6.20.0 | Navigation |
| React Hook Form | 7.48.2 | Form handling |
| React Hot Toast | 2.4.1 | Notifications |

### Database
- **SQLite** - Development & testing
- **PostgreSQL** - Production ready (optional)

### DevOps
- **Docker** - Containerization
- **GitHub Actions** - CI/CD
- **Nginx** - Reverse proxy

## 📁 Project Structure


## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- Node.js 16 or higher
- Git
- 4GB RAM minimum

### Installation Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/vishakha2121/customer-churn-prediction-system.git
cd customer-churn-prediction-system

# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env
# Edit .env with your configurations

# Initialize database
cd ../database
python init_db.py

# Generate sample data
cd ../scripts
python generate_sample_data.py

# Train ML models
python train_churn_model.py
python train_segmentation.py

# Start backend server
cd ../backend
python run.py

# Navigate to frontend
cd frontend

# Install dependencies
npm install

# Create .env file
echo "VITE_API_URL=http://localhost:8000/api" > .env

# Start development server
npm run dev