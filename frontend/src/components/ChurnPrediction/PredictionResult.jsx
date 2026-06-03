import React from 'react'
import { motion } from 'framer-motion'

const PredictionResult = ({ result }) => {
  if (!result) return null
  
  const getRiskColor = (risk) => {
    switch(risk) {
      case 'High': return 'text-red-500 bg-red-100 dark:bg-red-900/20'
      case 'Medium': return 'text-yellow-500 bg-yellow-100 dark:bg-yellow-900/20'
      case 'Low': return 'text-green-500 bg-green-100 dark:bg-green-900/20'
      default: return 'text-gray-500 bg-gray-100'
    }
  }
  
  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      className="mt-6 p-6 bg-gray-50 dark:bg-gray-700 rounded-xl"
    >
      <h3 className="text-lg font-semibold mb-4">Prediction Results</h3>
      
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="text-center p-4 bg-white dark:bg-gray-800 rounded-lg">
          <p className="text-sm text-gray-500 dark:text-gray-400">Churn Probability</p>
          <p className="text-3xl font-bold text-primary">{result.churn_probability}%</p>
        </div>
        
        <div className="text-center p-4 bg-white dark:bg-gray-800 rounded-lg">
          <p className="text-sm text-gray-500 dark:text-gray-400">Risk Level</p>
          <p className={`text-2xl font-bold ${getRiskColor(result.risk_level)} px-3 py-1 rounded-full inline-block mt-2`}>
            {result.risk_level}
          </p>
        </div>
        
        <div className="text-center p-4 bg-white dark:bg-gray-800 rounded-lg">
          <p className="text-sm text-gray-500 dark:text-gray-400">Confidence Score</p>
          <p className="text-3xl font-bold text-success">{result.confidence_score}%</p>
        </div>
      </div>
      
      {result.risk_level === 'High' && (
        <div className="mt-4 p-4 bg-red-50 dark:bg-red-900/20 rounded-lg">
          <p className="text-red-700 dark:text-red-300">
            ⚠️ High risk customer! Immediate retention action recommended.
          </p>
        </div>
      )}
    </motion.div>
  )
}

export default PredictionResult