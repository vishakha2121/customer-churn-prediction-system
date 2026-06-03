-- seed_strategies.sql
-- Insert additional retention strategies

INSERT OR IGNORE INTO retention_strategies (segment_id, strategy_name, offer_type, discount_percent, contract_upgrade, free_service_months, priority_support, success_rate, cost_per_customer, estimated_roi) VALUES
(0, 'Emergency Retention', 'discount', 30, 12, 2, 1, 75, 100, 250),
(0, 'Payment Plan Restructure', 'credit', 0, 6, 0, 0, 50, 40, 120),
(1, 'Loyalty Bonus', 'reward', 10, 12, 3, 1, 80, 60, 300),
(1, 'Referral Champion', 'referral', 0, 0, 0, 1, 65, 25, 180),
(2, 'Service Upgrade Special', 'service_upgrade', 20, 12, 1, 0, 55, 50, 150),
(2, 'Annual Plan Discount', 'discount', 15, 12, 0, 0, 60, 35, 140),
(3, 'First 3 Months Free', 'credit', 100, 12, 3, 1, 70, 120, 200),
(3, 'Setup Fee Waiver', 'discount', 50, 6, 0, 0, 65, 50, 160);