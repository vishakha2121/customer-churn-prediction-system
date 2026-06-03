FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY ../backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ../backend /app

# Create necessary directories
RUN mkdir -p /app/data/raw /app/data/processed /app/data/models /app/logs

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "run.py"]