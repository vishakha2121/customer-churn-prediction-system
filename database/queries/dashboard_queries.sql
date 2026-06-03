-- dashboard_queries.sql
-- Dashboard-specific queries

-- 1. Quick Stats (KPIs)
SELECT 
    (SELECT COUNT(*) FROM customers) as total_customers,
    (SELECT ROUND(AVG(churn_risk_score), 2) FROM customers) as avg_churn_risk,
    (SELECT COUNT(*) FROM customers WHERE churn_risk_score > 70) as high_risk_count,
    (SELECT ROUND(SUM(monthly_charges), 2) FROM customers WHERE churn_risk_score > 70) as revenue_at_risk,
    (SELECT COUNT(*) FROM simulations WHERE status = 'completed') as simulations_completed;

-- 2. Recent High Risk Customers
SELECT 
    customer_id,
    name,
    monthly_charges,
    churn_risk_score,
    contract_type
FROM customers
WHERE churn_risk_score > 70
ORDER BY churn_risk_score DESC
LIMIT 10;

-- 3. Daily Prediction Volume
SELECT 
    date(prediction_date) as pred_date,
    COUNT(*) as predictions_count,
    ROUND(AVG(churn_probability), 2) as avg_probability
FROM predictions
WHERE prediction_date >= date('now', '-30 days')
GROUP BY date(prediction_date)
ORDER BY pred_date DESC;

-- 4. Top Performing Strategies
SELECT 
    rs.strategy_name,
    rs.segment_id,
    s.segment_name,
    ROUND(AVG(rm.roi_percentage), 2) as avg_roi,
    SUM(rm.total_customers_saved) as total_saved
FROM roi_metrics rm
JOIN simulations sim ON rm.simulation_id = sim.simulation_id
JOIN retention_strategies rs ON sim.strategy_id = rs.strategy_id
JOIN segments s ON rs.segment_id = s.segment_id
GROUP BY rs.strategy_id
ORDER BY avg_roi DESC
LIMIT 5;

-- 5. Churn Trend by Week
SELECT 
    strftime('%Y-W%W', prediction_date) as week,
    COUNT(*) as predictions,
    ROUND(AVG(churn_probability), 2) as avg_churn,
    SUM(CASE WHEN churn_probability > 70 THEN 1 ELSE 0 END) as high_risk
FROM predictions
WHERE prediction_date >= date('now', '-90 days')
GROUP BY week
ORDER BY week;