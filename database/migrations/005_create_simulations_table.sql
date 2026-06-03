-- 005_create_simulations_table.sql
-- Create simulations table

CREATE TABLE IF NOT EXISTS simulations (
    simulation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    strategy_id INTEGER,
    target_segment_id INTEGER,
    num_customers_targeted INTEGER,
    expected_success_rate DECIMAL(5,2),
    expected_roi DECIMAL(10,2),
    estimated_savings DECIMAL(15,2),
    implementation_cost DECIMAL(15,2),
    breakeven_months DECIMAL(5,2),
    customers_saved INTEGER,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (strategy_id) REFERENCES retention_strategies(strategy_id),
    FOREIGN KEY (target_segment_id) REFERENCES segments(segment_id)
);

-- Create indexes
CREATE INDEX idx_simulations_strategy ON simulations(strategy_id);
CREATE INDEX idx_simulations_segment ON simulations(target_segment_id);
CREATE INDEX idx_simulations_date ON simulations(created_at);