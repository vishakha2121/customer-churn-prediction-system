import api from './api'

export const simulationService = {
  simulateROI: (data) => api.post('/simulation/roi/simulate', data),
  
  runScenario: (strategyName, segmentId, investment) =>
    api.post(`/simulation/roi/scenario?strategy_name=${strategyName}&target_segment=${segmentId}&investment_amount=${investment}`),
  
  getHistoricalROI: (strategyId) => api.get(`/simulation/roi/historical/${strategyId}`),
  
  optimizeAllocation: (targetRoi, maxBudget) =>
    api.post(`/simulation/roi/optimize?target_roi=${targetRoi}&max_budget=${maxBudget}`),
  
  getSimulationHistory: (limit = 10) => api.get(`/simulation/simulations/history?limit=${limit}`),
}