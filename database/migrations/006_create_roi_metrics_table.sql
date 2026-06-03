-- 006_create_roi_metrics_table.sql
-- Create ROI metrics table

CREATE TABLE IF NOT EXISTS roi_metrics (
    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
    simulation_id INTEGER,
    total_customers_saved INTEGER,
    revenue_saved DECIMAL(15,2),
    cost_incurred DECIMAL(15,2),
    net_savings DECIMAL(15,2),
    roi_percentage DECIMAL(10,2),
    payback_period DECIMAL(5,2),
    monthly_savings DECIMAL(15,2),
    calculated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (simulation_id) REFERENCES simulations(simulation_id)
);

-- Create indexes
CREATE INDEX idx_roi_simulation ON roi_metrics(simulation_id);
CREATE INDEX idx_roi_calculated ON roi_metrics(calculated_at);