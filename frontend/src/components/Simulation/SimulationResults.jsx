import React from 'react'
import { motion } from 'framer-motion'

const SimulationResults = ({ results }) => {
  if (!results) return null
  
  const isProfitable = results.roi_percentage > 0
  
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="space-y-6"
    >
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="text-center p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
          <p className="text-sm text-gray-600 dark:text-gray-400">ROI</p>
          <p className={`text-3xl font-bold ${isProfitable ? 'text-green-500' : 'text-red-500'}`}>
            {results.roi_percentage}%
          </p>
        </div>
        
        <div className="text-center p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
          <p className="text-sm text-gray-600 dark:text-gray-400">Net Savings</p>
          <p className="text-3xl font-bold text-blue-500">
            ${results.net_savings.toLocaleString()}
          </p>
        </div>
        
        <div className="text-center p-4 bg-purple-50 dark:bg-purple-900/20 rounded-lg">
          <p className="text-sm text-gray-600 dark:text-gray-400">Customers Saved</p>
          <p className="text-3xl font-bold text-purple-500">
            {results.customers_saved}
          </p>
        </div>
      </div>
      
      <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-6">
        <h3 className="font-semibold mb-3">Detailed Analysis</h3>
        <div className="space-y-2">
          <p>Total Investment: <span className="font-semibold">${results.total_cost.toLocaleString()}</span></p>
          <p>Revenue Retained: <span className="font-semibold">${results.revenue_retained.toLocaleString()}</span></p>
          <p>Breakeven Period: <span className="font-semibold">{results.breakeven_months} months</span></p>
        </div>
      </div>
      
      <div className={`p-4 rounded-lg ${isProfitable ? 'bg-green-100 dark:bg-green-900/20' : 'bg-red-100 dark:bg-red-900/20'}`}>
        <p className="font-semibold">
          {isProfitable 
            ? '✅ This strategy is profitable and recommended!' 
            : '⚠️ This strategy may not be profitable. Consider adjusting parameters.'}
        </p>
      </div>
    </motion.div>
  )
}

export default SimulationResults