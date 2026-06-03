#!/bin/bash

# Customer Churn Prediction System - Setup Script
# This script will set up the entire project from scratch

echo "========================================="
echo "Customer Churn Prediction System Setup"
echo "========================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
echo -e "\n${YELLOW}Checking Python version...${NC}"
python_version=$(python3 --version 2>&1 | grep -Po '(?<=Python )\d+\.\d+')
if [[ $(echo "$python_version >= 3.9" | bc) -ne 1 ]]; then
    echo -e "${RED}Python 3.9+ is required. Found: $python_version${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python $python_version found${NC}"

# Check Node.js version
echo -e "\n${YELLOW}Checking Node.js version...${NC}"
if ! command -v node &> /dev/null; then
    echo -e "${RED}Node.js is not installed. Please install Node.js 16+${NC}"
    exit 1
fi
node_version=$(node --version | cut -d'v' -f2)
echo -e "${GREEN}✓ Node.js v$node_version found${NC}"

# Create virtual environment
echo -e "\n${YELLOW}Setting up Python virtual environment...${NC}"
cd backend
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}✓ Backend dependencies installed${NC}"

# Setup frontend
echo -e "\n${YELLOW}Setting up frontend...${NC}"
cd ../frontend
npm install
echo -e "${GREEN}✓ Frontend dependencies installed${NC}"

# Initialize database
echo -e "\n${YELLOW}Initializing database...${NC}"
cd ../database
python3 init_db.py
echo -e "${GREEN}✓ Database initialized${NC}"

# Generate sample data
echo -e "\n${YELLOW}Generating sample data...${NC}"
cd ../scripts
python3 generate_sample_data.py
echo -e "${GREEN}✓ Sample data generated${NC}"

# Train models
echo -e "\n${YELLOW}Training ML models...${NC}"
python3 train_churn_model.py
python3 train_segmentation.py
echo -e "${GREEN}✓ Models trained successfully${NC}"

# Create .env files
echo -e "\n${YELLOW}Creating environment files...${NC}"
cd ..
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}✓ Root .env file created${NC}"
fi

if [ ! -f backend/.env ]; then
    cp backend/.env.example backend/.env
    echo -e "${GREEN}✓ Backend .env file created${NC}"
fi

if [ ! -f frontend/.env ]; then
    echo "VITE_API_URL=http://localhost:8000/api" > frontend/.env
    echo -e "${GREEN}✓ Frontend .env file created${NC}"
fi

echo -e "\n${GREEN}========================================="
echo "Setup Complete! 🎉"
echo "=========================================${NC}"

echo -e "\nTo start the application:"
echo -e "${YELLOW}1. Start Backend:${NC}"
echo "   cd backend && source venv/bin/activate && python run.py"
echo ""
echo -e "${YELLOW}2. Start Frontend (new terminal):${NC}"
echo "   cd frontend && npm run dev"
echo ""
echo -e "${YELLOW}3. Access the application:${NC}"
echo "   Frontend: http://localhost:3000"
echo "   Backend API: http://localhost:8000"
echo "   API Documentation: http://localhost:8000/docs"
echo ""

# Make script executable
chmod +x setup.sh