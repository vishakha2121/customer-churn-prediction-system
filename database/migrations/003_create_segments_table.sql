-- 003_create_segments_table.sql
-- Create segments table

CREATE TABLE IF NOT EXISTS segments (
    segment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    segment_name VARCHAR(100) NOT NULL,
    cluster_center_features TEXT,
    segment_size INTEGER DEFAULT 0,
    avg_churn_rate DECIMAL(5,2) DEFAULT 0,
    avg_tenure DECIMAL(10,2) DEFAULT 0,
    avg_monthly_charges DECIMAL(10,2) DEFAULT 0,
    avg_total_services DECIMAL(5,2) DEFAULT 0,
    month_to_month_pct DECIMAL(5,2) DEFAULT 0,
    electronic_check_pct DECIMAL(5,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert default segments
INSERT OR IGNORE INTO segments (segment_id, segment_name, avg_churn_rate, avg_tenure, avg_monthly_charges) VALUES
(0, 'High-Risk Customers', 68.5, 8.5, 85.30),
(1, 'Premium Loyal', 12.3, 36.2, 95.60),
(2, 'Value Seekers', 28.7, 18.5, 45.20),
(3, 'New Customers', 42.3, 3.2, 55.80);