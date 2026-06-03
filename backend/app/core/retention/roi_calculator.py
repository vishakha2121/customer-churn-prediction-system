from typing import Dict, List, Any
import numpy as np

class ROICalculator:
    def __init__(self):
        self.default_clv = 1200  # Average Customer Lifetime Value
        self.default_acquisition_cost = 300
    
    def calculate_roi(self, strategy_config: Dict, num_customers: int, success_rate: float, period_months: int) -> Dict:
        """Calculate ROI for a retention strategy"""
        
        # Calculate costs
        cost_per_customer = strategy_config.get('cost_per_customer', 50)
        total_cost = cost_per_customer * num_customers
        
        # Calculate benefits
        customers_saved = int(num_customers * (success_rate / 100))
        clv = strategy_config.get('customer_lifetime_value', self.default_clv)
        revenue_retained = customers_saved * clv
        
        # Calculate net savings
        net_savings = revenue_retained - total_cost
        
        # Calculate ROI percentage
        if total_cost > 0:
            roi_percentage = (net_savings / total_cost) * 100
        else:
            roi_percentage = 0
        
        # Calculate payback period (months)
        monthly_savings = revenue_retained / period_months
        if monthly_savings > 0:
            payback_months = total_cost / monthly_savings
        else:
            payback_months = float('inf')
        
        return {
            'total_cost': total_cost,
            'customers_saved': customers_saved,
            'revenue_retained': revenue_retained,
            'net_savings': net_savings,
            'roi_percentage': round(roi_percentage, 2),
            'payback_months': round(payback_months, 1),
            'breakeven_analysis': {
                'breakeven_customers': int(total_cost / clv) if clv > 0 else 0,
                'breakeven_revenue': total_cost
            }
        }
    
    def run_scenario_analysis(self, strategy: str, segment_id: int, investment: float) -> Dict:
        """Run what-if scenario analysis"""
        scenarios = []
        
        # Test different success rates
        success_rates = [20, 40, 60, 80]
        
        for rate in success_rates:
            # Estimate customers reachable with investment
            cost_per_customer = 50
            customers_reachable = int(investment / cost_per_customer) if cost_per_customer > 0 else 0
            
            # Calculate ROI
            strategy_config = {
                'cost_per_customer': cost_per_customer,
                'customer_lifetime_value': self.default_clv
            }
            
            result = self.calculate_roi(
                strategy_config,
                customers_reachable,
                rate,
                12
            )
            
            scenarios.append({
                'success_rate': rate,
                'customers_reachable': customers_reachable,
                'expected_roi': result['roi_percentage'],
                'net_savings': result['net_savings']
            })
        
        return {
            'strategy': strategy,
            'segment_id': segment_id,
            'investment_amount': investment,
            'scenarios': scenarios,
            'recommended_strategy': max(scenarios, key=lambda x: x['expected_roi'])
        }
    
    def get_historical_roi(self, strategy_id: int) -> Dict:
        """Get historical ROI data (mock implementation)"""
        # In real implementation, query database
        historical_data = {
            'last_3_months': [15.2, 22.8, 28.5],
            'average_roi': 22.17,
            'best_performing_segment': 1,
            'trend': 'increasing'
        }
        return historical_data
    
    def optimize_allocation(self, target_roi: float, budget_limit: float) -> Dict:
        """Optimize resource allocation across segments"""
        
        # Mock segment performance data
        segments = [
            {'id': 0, 'name': 'High Risk', 'expected_roi': 35, 'cost_per_customer': 80},
            {'id': 1, 'name': 'Medium Risk', 'expected_roi': 25, 'cost_per_customer': 50},
            {'id': 2, 'name': 'Low Risk', 'expected_roi': 15, 'cost_per_customer': 30},
            {'id': 3, 'name': 'Premium', 'expected_roi': 20, 'cost_per_customer': 60}
        ]
        
        # Sort by ROI efficiency
        for seg in segments:
            seg['efficiency'] = seg['expected_roi'] / seg['cost_per_customer']
        
        sorted_segments = sorted(segments, key=lambda x: x['efficiency'], reverse=True)
        
        # Allocate budget
        allocation = []
        remaining_budget = budget_limit
        
        for segment in sorted_segments:
            if remaining_budget <= 0:
                break
            
            # Allocate to this segment
            max_customers = remaining_budget // segment['cost_per_customer']
            allocated_budget = max_customers * segment['cost_per_customer']
            
            if allocated_budget > 0:
                allocation.append({
                    'segment_id': segment['id'],
                    'segment_name': segment['name'],
                    'customers': max_customers,
                    'budget': allocated_budget,
                    'expected_roi': segment['expected_roi']
                })
                remaining_budget -= allocated_budget
        
        # Calculate overall ROI
        total_investment = budget_limit - remaining_budget
        weighted_roi = sum(a['expected_roi'] * a['budget'] for a in allocation) / total_investment if total_investment > 0 else 0
        
        return {
            'total_budget': budget_limit,
            'allocated_budget': total_investment,
            'unallocated_budget': remaining_budget,
            'expected_overall_roi': round(weighted_roi, 2),
            'meets_target': weighted_roi >= target_roi,
            'allocation_details': allocation
        }