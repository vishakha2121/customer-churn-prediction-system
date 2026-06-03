-- 002_create_predictions_table.sql
-- Create predictions table

CREATE TABLE IF NOT EXISTS predictions (
    prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    churn_probability DECIMAL(5,2) NOT NULL,
    predicted_churn_date DATE,
    confidence_score DECIMAL(5,2),
    model_version VARCHAR(50),
    prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_accurate BOOLEAN DEFAULT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Create indexes
CREATE INDEX idx_predictions_customer ON predictions(customer_id);
CREATE INDEX idx_predictions_date ON predictions(prediction_date);
CREATE INDEX idx_predictions_probability ON predictions(churn_probability);