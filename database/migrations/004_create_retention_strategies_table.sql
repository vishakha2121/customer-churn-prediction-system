-- 004_create_retention_strategies_table.sql
-- Create retention strategies table

CREATE TABLE IF NOT EXISTS retention_strategies (
    strategy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    segment_id INTEGER,
    strategy_name VARCHAR(200) NOT NULL,
    offer_type VARCHAR(50),
    discount_percent DECIMAL(5,2) DEFAULT 0,
    contract_upgrade INTEGER DEFAULT 0,
    free_service_months INTEGER DEFAULT 0,
    priority_support BOOLEAN DEFAULT FALSE,
    success_rate DECIMAL(5,2),
    cost_per_customer DECIMAL(10,2),
    estimated_roi DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (segment_id) REFERENCES segments(segment_id)
);

-- Insert default strategies
INSERT OR IGNORE INTO retention_strategies (segment_id, strategy_name, offer_type, discount_percent, contract_upgrade, priority_support, success_rate, cost_per_customer) VALUES
(0, 'Immediate Retention Offer', 'discount', 25, 12, 1, 65, 80),
(0, 'Personalized Win-back', 'discount', 20, 6, 0, 55, 60),
(1, 'Premium Rewards Program', 'reward', 15, 6, 1, 75, 50),
(1, 'VIP Status Upgrade', 'service_upgrade', 0, 12, 1, 70, 40),
(2, 'Value Bundle', 'bundle', 10, 12, 0, 60, 40),
(2, 'Referral Program', 'referral', 5, 0, 0, 50, 30),
(3, 'Onboarding Support', 'support', 0, 0, 1, 55, 30),
(3, 'Welcome Discount', 'discount', 15, 6, 0, 60, 35);