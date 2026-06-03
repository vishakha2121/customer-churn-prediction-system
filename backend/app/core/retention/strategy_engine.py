from typing import List, Dict, Any
import random

class StrategyEngine:
    def __init__(self):
        self.strategy_templates = {
            'high_risk': [
                {
                    'name': 'Immediate Retention Offer',
                    'description': 'High-value discount + priority support',
                    'discount': 25,
                    'contract_required': 12,
                    'priority_support': True,
                    'estimated_success': 0.65
                },
                {
                    'name': 'Personalized Win-back',
                    'description': 'Custom offer based on usage patterns',
                    'discount': 20,
                    'contract_required': 6,
                    'priority_support': False,
                    'estimated_success': 0.55
                }
            ],
            'medium_risk': [
                {
                    'name': 'Loyalty Rewards',
                    'description': 'Points program + service upgrade',
                    'discount': 15,
                    'contract_required': 6,
                    'priority_support': False,
                    'estimated_success': 0.70
                },
                {
                    'name': 'Service Bundle',
                    'description': 'Free service addition with contract',
                    'discount': 10,
                    'contract_required': 12,
                    'priority_support': False,
                    'estimated_success': 0.60
                }
            ],
            'low_risk': [
                {
                    'name': 'Referral Program',
                    'description': 'Incentives for referrals',
                    'discount': 5,
                    'contract_required': 0,
                    'priority_support': False,
                    'estimated_success': 0.50
                },
                {
                    'name': 'Feature Upgrade',
                    'description': 'Free premium features trial',
                    'discount': 0,
                    'contract_required': 0,
                    'priority_support': False,
                    'estimated_success': 0.45
                }
            ]
        }
    
    def generate_strategies_for_segment(self, segment_id: int) -> List[Dict]:
        """Generate retention strategies based on segment characteristics"""
        # For demo, map segment_id to risk level
        risk_levels = {
            0: 'high_risk',
            1: 'medium_risk',
            2: 'low_risk',
            3: 'medium_risk'
        }
        
        risk_level = risk_levels.get(segment_id % 4, 'medium_risk')
        strategies = self.strategy_templates[risk_level].copy()
        
        # Add segment-specific customization
        for strategy in strategies:
            strategy['segment_id'] = segment_id
            strategy['estimated_roi'] = round(strategy['estimated_success'] * 100 * random.uniform(0.8, 1.2), 2)
        
        return strategies
    
    def customize_strategy(self, segment_id: int, budget: float = None, timeline: int = 30) -> Dict:
        """Customize strategies based on constraints"""
        strategies = self.generate_strategies_for_segment(segment_id)
        
        if budget:
            # Filter strategies within budget
            strategies = [s for s in strategies if s.get('cost', 0) <= budget]
        
        return {
            'segment_id': segment_id,
            'customized_strategies': strategies,
            'budget_constraint': budget,
            'timeline_days': timeline,
            'total_strategies': len(strategies)
        }
    
    def compare_strategies(self, segment_ids: List[int]) -> Dict:
        """Compare strategies across multiple segments"""
        comparison = {}
        
        for segment_id in segment_ids:
            strategies = self.generate_strategies_for_segment(segment_id)
            comparison[segment_id] = {
                'strategies': strategies,
                'avg_estimated_success': sum(s['estimated_success'] for s in strategies) / len(strategies),
                'best_strategy': max(strategies, key=lambda x: x['estimated_success'])
            }
        
        return comparison