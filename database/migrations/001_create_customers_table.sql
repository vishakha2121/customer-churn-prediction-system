-- 001_create_customers_table.sql
-- Create customers table

CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100),
    email VARCHAR(100),
    age INTEGER,
    gender VARCHAR(10),
    tenure_months INTEGER NOT NULL,
    monthly_charges DECIMAL(10,2) NOT NULL,
    total_charges DECIMAL(10,2) NOT NULL,
    contract_type VARCHAR(50) NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    paperless_billing BOOLEAN NOT NULL,
    internet_service VARCHAR(50),
    online_security VARCHAR(50),
    online_backup VARCHAR(50),
    device_protection VARCHAR(50),
    tech_support VARCHAR(50),
    streaming_tv VARCHAR(50),
    streaming_movies VARCHAR(50),
    churn_risk_score DECIMAL(5,2) DEFAULT 0,
    segment_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (segment_id) REFERENCES segments(segment_id)
);

-- Create indexes
CREATE INDEX idx_customers_customer_id ON customers(customer_id);
CREATE INDEX idx_customers_contract_type ON customers(contract_type);
CREATE INDEX idx_customers_tenure ON customers(tenure_months);
CREATE INDEX idx_customers_segment ON customers(segment_id);