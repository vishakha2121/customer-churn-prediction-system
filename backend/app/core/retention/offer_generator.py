from typing import List, Dict, Any
import uuid
from datetime import datetime, timedelta

class OfferGenerator:
    def __init__(self):
        self.offers = []
        self.active_offers = {}
    
    def generate_offers(self, segment_id: int, limit: int = 5) -> List[Dict]:
        """Generate specific offers for a segment"""
        offers = []
        
        # Offer templates by segment type
        offer_templates = {
            'premium': [
                {
                    'type': 'discount',
                    'name': 'Premium Plus Discount',
                    'value': 25,
                    'duration_months': 6,
                    'conditions': ['12-month contract', 'Auto-pay enrollment']
                },
                {
                    'type': 'service_upgrade',
                    'name': 'Free Speed Upgrade',
                    'value': '500 Mbps',
                    'duration_months': 12,
                    'conditions': ['24-month contract']
                }
            ],
            'at_risk': [
                {
                    'type': 'discount',
                    'name': 'Retention Discount',
                    'value': 30,
                    'duration_months': 3,
                    'conditions': ['6-month contract']
                },
                {
                    'type': 'credit',
                    'name': 'Loyalty Credit',
                    'value': 50,
                    'duration_months': 1,
                    'conditions': ['No contract required']
                }
            ],
            'loyal': [
                {
                    'type': 'reward',
                    'name': 'VIP Status',
                    'value': 'Priority support + Exclusive offers',
                    'duration_months': 12,
                    'conditions': ['Maintain current service']
                },
                {
                    'type': 'referral',
                    'name': 'Referral Bonus',
                    'value': 100,
                    'duration_months': 0,
                    'conditions': ['Refer a friend']
                }
            ]
        }
        
        # Determine segment type
        segment_type = self._get_segment_type(segment_id)
        templates = offer_templates.get(segment_type, offer_templates['at_risk'])
        
        for i in range(min(limit, len(templates))):
            template = templates[i % len(templates)]
            offer = {
                'offer_id': str(uuid.uuid4())[:8],
                'segment_id': segment_id,
                'offer_type': template['type'],
                'offer_name': template['name'],
                'value': template['value'],
                'duration_months': template['duration_months'],
                'conditions': template['conditions'],
                'expiry_date': (datetime.now() + timedelta(days=30)).isoformat(),
                'estimated_acceptance_rate': self._calculate_acceptance_rate(segment_id, template['type'])
            }
            offers.append(offer)
        
        return offers
    
    def _get_segment_type(self, segment_id: int) -> str:
        """Map segment ID to type"""
        types = ['at_risk', 'premium', 'loyal', 'at_risk']
        return types[segment_id % len(types)]
    
    def _calculate_acceptance_rate(self, segment_id: int, offer_type: str) -> float:
        """Calculate estimated acceptance rate"""
        base_rates = {
            'discount': 0.65,
            'service_upgrade': 0.45,
            'credit': 0.70,
            'reward': 0.50,
            'referral': 0.35
        }
        
        base_rate = base_rates.get(offer_type, 0.5)
        
        # Segment adjustment
        if segment_id == 0:  # High risk
            base_rate *= 1.2
        elif segment_id == 2:  # Low risk
            base_rate *= 0.8
        
        return min(base_rate, 0.95)
    
    def apply_offer(self, customer_id: str, offer_id: str) -> Dict:
        """Apply an offer to a customer"""
        # Find offer
        offer = self._find_offer(offer_id)
        if not offer:
            return {'success': False, 'error': 'Offer not found'}
        
        # Apply offer to customer
        self.active_offers[customer_id] = {
            'offer_id': offer_id,
            'applied_at': datetime.now().isoformat(),
            'status': 'active',
            'expires_at': offer['expiry_date']
        }
        
        return {
            'success': True,
            'message': f"Offer {offer['offer_name']} applied successfully",
            'customer_id': customer_id,
            'offer_details': offer
        }
    
    def _find_offer(self, offer_id: str) -> Dict:
        """Find offer by ID (mock implementation)"""
        # In real implementation, search database
        return {
            'offer_name': 'Retention Discount',
            'offer_type': 'discount',
            'value': 30,
            'expiry_date': (datetime.now() + timedelta(days=30)).isoformat()
        }