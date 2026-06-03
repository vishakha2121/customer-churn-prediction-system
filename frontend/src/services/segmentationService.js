import api from './api'

export const segmentationService = {
  getSegments: () => api.get('/segmentation/segments'),
  
  getSegmentById: (segmentId) => api.get(`/segmentation/segment/${segmentId}`),
  
  assignCustomer: (customerId) => api.post('/segmentation/assign', { customer_id: customerId }),
  
  getSegmentCharacteristics: (segmentId) => api.get(`/segmentation/characteristics/${segmentId}`),
  
  getSegmentPerformance: () => api.get('/dashboard/segment/performance'),
}