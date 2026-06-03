import React, { useState } from 'react'
import axios from 'axios'
import toast from 'react-hot-toast'

const ChurnPredictionPage = () => {
  const [formData, setFormData] = useState({
    customer_id: '',
    tenure_months: 12,
    monthly_charges: 70.5,
    total_charges: 846,
    contract_type: 'Month-to-month',
    payment_method: 'Electronic check',
    paperless_billing: true,
    internet_service: 'Fiber optic',
    online_security: 'No',
    online_backup: 'No',
    device_protection: 'No',
    tech_support: 'No',
    streaming_tv: 'Yes',
    streaming_movies: 'Yes'
  })
  
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  
  const handleSubmit = async (e) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      const response = await axios.post('http://localhost:8000/api/churn/predict', formData)
      setResult(response.data)
      toast.success('Prediction completed!')
    } catch (error) {
      console.error('Error:', error)
      toast.error('Prediction failed. Make sure backend is running on port 8000')
    } finally {
      setLoading(false)
    }
  }
  
  const getRiskColor = (risk) => {
    if (risk === 'High') return 'text-red-600 bg-red-100'
    if (risk === 'Medium') return 'text-yellow-600 bg-yellow-100'
    return 'text-green-600 bg-green-100'
  }
  
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Churn Prediction</h1>
      <p className="text-gray-600 dark:text-gray-400">Predict customer churn probability using AI</p>
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h2 className="text-lg font-semibold mb-4">Customer Information</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="block text-sm font-medium mb-1">Customer ID</label>
              <input
                type="text"
                value={formData.customer_id}
                onChange={(e) => setFormData({...formData, customer_id: e.target.value})}
                className="input-field"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Tenure (months)</label>
              <input
                type="number"
                value={formData.tenure_months}
                onChange={(e) => setFormData({...formData, tenure_months: parseInt(e.target.value)})}
                className="input-field"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Monthly Charges ($)</label>
              <input
                type="number"
                step="0.01"
                value={formData.monthly_charges}
                onChange={(e) => setFormData({...formData, monthly_charges: parseFloat(e.target.value)})}
                className="input-field"
                required
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-1">Contract Type</label>
              <select
                value={formData.contract_type}
                onChange={(e) => setFormData({...formData, contract_type: e.target.value})}
                className="input-field"
              >
                <option>Month-to-month</option>
                <option>One year</option>
                <option>Two year</option>
              </select>
            </div>
            <button type="submit" disabled={loading} className="btn-primary w-full">
              {loading ? 'Predicting...' : 'Predict Churn Risk'}
            </button>
          </form>
        </div>
        
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h2 className="text-lg font-semibold mb-4">Prediction Results</h2>
          {result ? (
            <div className="space-y-4">
              <div className="text-center p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                <p className="text-sm text-gray-500">Churn Probability</p>
                <p className="text-4xl font-bold text-indigo-600">{result.churn_probability}%</p>
              </div>
              <div className="text-center p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
                <p className="text-sm text-gray-500">Risk Level</p>
                <p className={`text-2xl font-bold ${getRiskColor(result.risk_level)} px-4 py-2 rounded-full inline-block`}>
                  {result.risk_level}
                </p>
              </div>
              {result.risk_level === 'High' && (
                <div className="p-4 bg-red-50 dark:bg-red-900/20 rounded-lg">
                  <p className="text-red-700">⚠️ High risk customer! Immediate retention action recommended.</p>
                </div>
              )}
            </div>
          ) : (
            <div className="text-center py-12 text-gray-500">
              <p className="text-6xl mb-4">🔮</p>
              <p>Enter customer details and click predict</p>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default ChurnPredictionPage