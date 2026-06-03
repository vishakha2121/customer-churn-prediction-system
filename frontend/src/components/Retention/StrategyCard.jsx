import React from 'react'
import { motion } from 'framer-motion'
import { CheckCircleIcon, CurrencyDollarIcon, CalendarIcon } from '@heroicons/react/24/outline'

const StrategyCard = ({ strategy, onApply }) => {
  const getSuccessColor = (rate) => {
    if (rate >= 70) return 'text-green-500'
    if (rate >= 50) return 'text-yellow-500'
    return 'text-red-500'
  }
  
  return (
    <motion.div
      whileHover={{ y: -5 }}
      className="bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-hidden"
    >
      <div className="p-6">
        <div className="flex justify-between items-start mb-4">
          <h3 className="text-xl font-semibold">{strategy.strategy_name}</h3>
          <span className={`px-3 py-1 rounded-full text-sm font-medium ${getSuccessColor(strategy.estimated_success)} bg-opacity-10 bg-current`}>
            {strategy.estimated_success}% success
          </span>
        </div>
        
        <p className="text-gray-600 dark:text-gray-400 mb-4">{strategy.description}</p>
        
        <div className="space-y-2 mb-6">
          <div className="flex items-center text-sm">
            <CurrencyDollarIcon className="h-4 w-4 mr-2 text-gray-500" />
            <span>{strategy.discount}% discount</span>
          </div>
          <div className="flex items-center text-sm">
            <CalendarIcon className="h-4 w-4 mr-2 text-gray-500" />
            <span>{strategy.contract_required} month contract required</span>
          </div>
          {strategy.priority_support && (
            <div className="flex items-center text-sm">
              <CheckCircleIcon className="h-4 w-4 mr-2 text-green-500" />
              <span>Priority support included</span>
            </div>
          )}
        </div>
        
        <button
          onClick={() => onApply(strategy)}
          className="w-full btn-primary py-2"
        >
          Apply Strategy
        </button>
      </div>
    </motion.div>
  )
}

export default StrategyCard