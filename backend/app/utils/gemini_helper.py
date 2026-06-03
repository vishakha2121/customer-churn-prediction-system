import google.generativeai as genai
from app.config import settings
import logging

logger = logging.getLogger(__name__)

class GeminiHelper:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
            self.enabled = True
        else:
            self.enabled = False
            logger.warning("Gemini API key not configured")
    
    def generate_strategy_recommendations(self, segment_data: dict) -> str:
        """Generate retention strategy recommendations using Gemini"""
        if not self.enabled:
            return self._mock_recommendations(segment_data)
        
        try:
            prompt = f"""
            Based on this customer segment data, suggest 3 retention strategies:
            Segment: {segment_data.get('segment_name')}
            Churn Rate: {segment_data.get('avg_churn_rate')}%
            Avg Tenure: {segment_data.get('avg_tenure')} months
            Avg Monthly Charges: ${segment_data.get('avg_monthly_charges')}
            
            Provide specific, actionable recommendations.
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            return self._mock_recommendations(segment_data)
    
    def _mock_recommendations(self, segment_data: dict) -> str:
        """Mock recommendations when Gemini is not available"""
        churn_rate = segment_data.get('avg_churn_rate', 0)
        
        if churn_rate > 50:
            return """1. Immediate Intervention: Offer 25% discount with priority support for next 6 months
2. Personalized Outreach: Assign dedicated account manager for high-risk customers
3. Service Bundle: Add free premium services for 3 months to increase stickiness"""
        elif churn_rate > 30:
            return """1. Loyalty Program: Launch points-based rewards system
2. Contract Incentives: Offer 15% discount for 12-month commitment
3. Feature Education: Webinars to showcase underutilized features"""
        else:
            return """1. Referral Program: $50 credit for each successful referral
2. VIP Status: Early access to new features and priority support
3. Annual Plan Discount: 10% off for annual prepayment"""
    
    def analyze_churn_reasons(self, customer_data: dict) -> str:
        """Analyze potential churn reasons"""
        if not self.enabled:
            return "High monthly charges and month-to-month contract increase churn risk"
        
        try:
            prompt = f"""
            Analyze why this customer might churn and suggest solutions:
            Tenure: {customer_data.get('tenure_months')} months
            Contract: {customer_data.get('contract_type')}
            Monthly Charges: ${customer_data.get('monthly_charges')}
            Services: Online Security: {customer_data.get('online_security')}, Tech Support: {customer_data.get('tech_support')}
            """
            
            response = self.model.generate_content(prompt)
            return response.text
        except:
            return "Unable to analyze at this time"