-- analytics.sql
-- Analytical queries for churn analysis

-- 1. Churn Rate by Contract Type
SELECT 
    contract_type,
    COUNT(*) as total_customers,
    SUM(CASE WHEN churn_risk_score > 70 THEN 1 ELSE 0 END) as high_risk_count,
    ROUND(AVG(churn_risk_score), 2) as avg_risk_score
FROM customers
GROUP BY contract_type
ORDER BY avg_risk_score DESC;

-- 2. Customer Tenure Distribution
SELECT 
    CASE 
        WHEN tenure_months < 6 THEN '0-6 months'
        WHEN tenure_months < 12 THEN '6-12 months'
        WHEN tenure_months < 24 THEN '12-24 months'
        WHEN tenure_months < 48 THEN '24-48 months'
        ELSE '48+ months'
    END as tenure_group,
    COUNT(*) as customer_count,
    ROUND(AVG(monthly_charges), 2) as avg_monthly_charges,
    ROUND(AVG(churn_risk_score), 2) as avg_risk
FROM customers
GROUP BY tenure_group
ORDER BY MIN(tenure_months);

-- 3. Payment Method Churn Analysis
SELECT 
    payment_method,
    COUNT(*) as customer_count,
    ROUND(AVG(churn_risk_score), 2) as avg_risk,
    ROUND(AVG(monthly_charges), 2) as avg_charges
FROM customers
GROUP BY payment_method
ORDER BY avg_risk DESC;

-- 4. Service Adoption Impact
SELECT 
    CASE 
        WHEN online_security = 'Yes' AND tech_support = 'Yes' THEN 'Both Services'
        WHEN online_security = 'Yes' OR tech_support = 'Yes' THEN 'One Service'
        ELSE 'No Services'
    END as service_level,
    COUNT(*) as customer_count,
    ROUND(AVG(churn_risk_score), 2) as avg_risk
FROM customers
GROUP BY service_level
ORDER BY avg_risk;

-- 5. Monthly Revenue at Risk
SELECT 
    SUM(monthly_charges) as total_monthly_revenue,
    SUM(CASE WHEN churn_risk_score > 70 THEN monthly_charges ELSE 0 END) as revenue_at_risk,
    ROUND(100.0 * SUM(CASE WHEN churn_risk_score > 70 THEN monthly_charges ELSE 0 END) / SUM(monthly_charges), 2) as risk_percentage
FROM customers;