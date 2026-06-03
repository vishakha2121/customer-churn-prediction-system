import api from './api'

export const churnService = {
  predictSingle: (data) => api.post('/churn/predict', data),
  
  batchPredict: async (file) => {
    const formData = new FormData()
    formData.append('file', file)
    
    const response = await fetch(`${api.defaults.baseURL}/upload/customers/csv`, {
      method: 'POST',
      body: formData,
    })
    
    return response.json()
  },
  
  getModelAccuracy: () => api.get('/churn/model/accuracy'),
  
  getFeatureImportance: () => api.get('/churn/features/importance'),
}