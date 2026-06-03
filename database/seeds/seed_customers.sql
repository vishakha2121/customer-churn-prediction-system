-- seed_customers.sql
-- Insert sample customers

INSERT OR IGNORE INTO customers (customer_id, name, email, age, gender, tenure_months, monthly_charges, total_charges, contract_type, payment_method, paperless_billing, internet_service, online_security, online_backup, device_protection, tech_support, streaming_tv, streaming_movies) VALUES
('CUST0001', 'John Smith', 'john.smith@email.com', 35, 'Male', 12, 70.50, 846.00, 'Month-to-month', 'Electronic check', 1, 'Fiber optic', 'No', 'No', 'No', 'No', 'Yes', 'Yes'),
('CUST0002', 'Sarah Johnson', 'sarah.j@email.com', 42, 'Female', 24, 85.20, 2044.80, 'One year', 'Bank transfer', 0, 'DSL', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes'),
('CUST0003', 'Michael Brown', 'michael.b@email.com', 28, 'Male', 36, 95.30, 3430.80, 'Two year', 'Credit card', 0, 'Fiber optic', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'),
('CUST0004', 'Emily Davis', 'emily.d@email.com', 55, 'Female', 3, 45.60, 136.80, 'Month-to-month', 'Mailed check', 1, 'DSL', 'No', 'No', 'No', 'No', 'No', 'No'),
('CUST0005', 'David Wilson', 'david.w@email.com', 48, 'Male', 48, 65.80, 3158.40, 'One year', 'Bank transfer', 0, 'DSL', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes'),
('CUST0006', 'Lisa Anderson', 'lisa.a@email.com', 31, 'Female', 8, 89.50, 716.00, 'Month-to-month', 'Electronic check', 1, 'Fiber optic', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes'),
('CUST0007', 'James Taylor', 'james.t@email.com', 62, 'Male', 60, 55.20, 3312.00, 'Two year', 'Credit card', 0, 'DSL', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No'),
('CUST0008', 'Maria Garcia', 'maria.g@email.com', 29, 'Female', 15, 78.90, 1183.50, 'Month-to-month', 'Electronic check', 1, 'Fiber optic', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes'),
('CUST0009', 'Robert Martinez', 'robert.m@email.com', 45, 'Male', 30, 62.30, 1869.00, 'One year', 'Bank transfer', 0, 'DSL', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes'),
('CUST0010', 'Jennifer Lee', 'jennifer.l@email.com', 38, 'Female', 20, 95.00, 1900.00, 'One year', 'Credit card', 1, 'Fiber optic', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes');