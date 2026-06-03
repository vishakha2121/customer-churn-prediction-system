export const CONTRACT_TYPES = ['Month-to-month', 'One year', 'Two year']

export const PAYMENT_METHODS = ['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card']

export const INTERNET_SERVICES = ['DSL', 'Fiber optic', 'No']

export const SERVICE_OPTIONS = [
  'online_security',
  'online_backup',
  'device_protection',
  'tech_support',
  'streaming_tv',
  'streaming_movies'
]

export const CHURN_RISK_LEVELS = {
  HIGH: { min: 70, color: '#ef4444', label: 'High Risk' },
  MEDIUM: { min: 40, color: '#f59e0b', label: 'Medium Risk' },
  LOW: { min: 0, color: '#10b981', label: 'Low Risk' }
}

export const API_ENDPOINTS = {
  CHURN_PREDICT: '/churn/predict',
  CHURN_BATCH: '/churn/predict/batch',
  SEGMENTS: '/segmentation/segments',
  STRATEGIES: '/retention/strategies',
  SIMULATE: '/simulation/roi/simulate',
  DASHBOARD_KPIS: '/dashboard/kpis'
}