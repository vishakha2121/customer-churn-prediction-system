import api from './api'

export const retentionService = {
  getStrategies: (segmentId) => api.get(`/retention/strategies/${segmentId}`),
  
  customizeStrategy: (segmentId, budget, timeline) => 
    api.post(`/retention/strategies/customize?segment_id=${segmentId}&budget=${budget}&timeline=${timeline}`),
  
  getOffers: (segmentId, limit = 5) => 
    api.get(`/retention/offers/${segmentId}?limit=${limit}`),
  
  applyOffer: (customerId, offerId) => 
    api.post('/retention/offers/apply', { customer_id: customerId, offer_id: offerId }),
  
  compareStrategies: (segmentIds) => 
    api.get(`/retention/strategies/compare?segment_ids=${segmentIds.join(',')}`),
}