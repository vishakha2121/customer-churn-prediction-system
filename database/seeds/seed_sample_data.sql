-- seed_sample_data.sql
-- Insert sample simulation and ROI data

-- Insert sample simulations
INSERT OR IGNORE INTO simulations (strategy_id, target_segment_id, num_customers_targeted, expected_success_rate, expected_roi, estimated_savings, implementation_cost, breakeven_months, customers_saved, status) VALUES
(1, 0, 500, 65, 185, 92500, 40000, 5.2, 325, 'completed'),
(2, 0, 300, 55, 145, 43500, 18000, 4.8, 165, 'completed'),
(3, 1, 1000, 75, 220, 220000, 60000, 3.3, 750, 'completed'),
(5, 2, 800, 60, 165, 132000, 32000, 2.9, 480, 'in_progress');

-- Insert sample ROI metrics
INSERT OR IGNORE INTO roi_metrics (simulation_id, total_customers_saved, revenue_saved, cost_incurred, net_savings, roi_percentage, payback_period, monthly_savings) VALUES
(1, 325, 390000, 40000, 350000, 875, 1.2, 32500),
(2, 165, 198000, 18000, 180000, 1000, 0.9, 16500),
(3, 750, 900000, 60000, 840000, 1400, 0.8, 75000),
(4, 480, 576000, 32000, 544000, 1700, 0.7, 48000);