-- reports.sql
-- Report generation queries

-- 1. Monthly Churn Report
SELECT 
    strftime('%Y-%m', prediction_date) as month,
    COUNT(*) as total_predictions,
    ROUND(AVG(churn_probability), 2) as avg_churn_probability,
    SUM(CASE WHEN churn_probability > 70 THEN 1 ELSE 0 END) as high_risk_count
FROM predictions
GROUP BY month
ORDER BY month DESC
LIMIT 12;

-- 2. Segment Performance Report
SELECT 
    s.segment_name,
    COUNT(c.id) as customer_count,
    ROUND(AVG(c.monthly_charges), 2) as avg_revenue,
    ROUND(AVG(c.churn_risk_score), 2) as avg_risk,
    ROUND(s.avg_churn_rate, 2) as historical_churn
FROM segments s
LEFT JOIN customers c ON s.segment_id = c.segment_id
GROUP BY s.segment_id
ORDER BY avg_risk DESC;

-- 3. Strategy Effectiveness Report
SELECT 
    rs.strategy_name,
    COUNT(s.simulation_id) as times_used,
    ROUND(AVG(s.expected_roi), 2) as avg_roi,
    ROUND(AVG(s.customers_saved), 0) as avg_customers_saved,
    ROUND(AVG(rm.roi_percentage), 2) as actual_roi
FROM retention_strategies rs
LEFT JOIN simulations s ON rs.strategy_id = s.strategy_id
LEFT JOIN roi_metrics rm ON s.simulation_id = rm.simulation_id
GROUP BY rs.strategy_id
ORDER BY avg_roi DESC;

-- 4. Customer Lifetime Value Analysis
SELECT 
    segment_id,
    COUNT(*) as customer_count,
    ROUND(AVG(monthly_charges * tenure_months), 2) as avg_clv,
    ROUND(SUM(monthly_charges * tenure_months), 2) as total_clv
FROM customers
GROUP BY segment_id
ORDER BY avg_clv DESC;

-- 5. Retention ROI Summary
SELECT 
    rs.segment_id,
    s.segment_name,
    COUNT(rm.metric_id) as simulations_run,
    ROUND(AVG(rm.roi_percentage), 2) as avg_roi,
    ROUND(SUM(rm.net_savings), 2) as total_savings
FROM roi_metrics rm
JOIN simulations sim ON rm.simulation_id = sim.simulation_id
JOIN retention_strategies rs ON sim.strategy_id = rs.strategy_id
JOIN segments s ON rs.segment_id = s.segment_id
GROUP BY rs.segment_id;