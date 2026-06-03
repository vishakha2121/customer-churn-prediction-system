from typing import Dict, List, Any
import uuid
from datetime import datetime
import numpy as np
from app.core.retention.roi_calculator import ROICalculator

class SimulationService:
    def __init__(self):
        self.roi_calculator = ROICalculator()
        self.simulations_history = []
    
    def simulate_retention_impact(self, request) -> Dict:
        """Simulate the impact of retention strategies"""
        # Calculate ROI
        strategy_config = {
            'cost_per_customer': request.strategy.cost_per_customer,
            'customer_lifetime_value': 1200
        }
        
        roi_result = self.roi_calculator.calculate_roi(
            strategy_config,
            request.num_customers_to_target,
            request.expected_success_rate,
            request.simulation_period_months
        )
        
        # Generate simulation ID
        simulation_id = str(uuid.uuid4())[:8]
        
        # Store simulation
        simulation = {
            'id': simulation_id,
            'timestamp': datetime.now().isoformat(),
            'strategy': request.strategy.dict(),
            'num_customers': request.num_customers_to_target,
            'success_rate': request.expected_success_rate,
            'period_months': request.simulation_period_months,
            'roi_percentage': roi_result['roi_percentage'],
            'net_savings': roi_result['net_savings'],
            'breakeven_months': roi_result['payback_months'],
            'customers_saved': roi_result['customers_saved'],
            'total_cost': roi_result['total_cost'],
            'revenue_retained': roi_result['revenue_retained']
        }
        
        self.simulations_history.insert(0, simulation)
        
        # Keep only last 100 simulations
        self.simulations_history = self.simulations_history[:100]
        
        return simulation
    
    def get_simulation_history(self, limit: int = 10) -> List[Dict]:
        """Get history of previous simulations"""
        return self.simulations_history[:limit]
    
    def compare_strategies(self, strategies: List[Dict]) -> Dict:
        """Compare multiple strategies"""
        comparisons = []
        
        for strategy in strategies:
            roi = self.roi_calculator.calculate_roi(
                {'cost_per_customer': strategy.get('cost', 50), 'customer_lifetime_value': 1200},
                strategy.get('num_customers', 1000),
                strategy.get('success_rate', 50),
                12
            )
            
            comparisons.append({
                'strategy_name': strategy.get('name', 'Unknown'),
                'roi_percentage': roi['roi_percentage'],
                'net_savings': roi['net_savings'],
                'customers_saved': roi['customers_saved']
            })
        
        # Find best strategy
        best = max(comparisons, key=lambda x: x['roi_percentage'])
        
        return {
            'comparisons': comparisons,
            'best_strategy': best,
            'recommendation': f"Strategy '{best['strategy_name']}' gives highest ROI at {best['roi_percentage']}%"
        }