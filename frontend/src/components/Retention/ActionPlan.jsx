import React from 'react'
import { motion } from 'framer-motion'

const ActionPlan = ({ plan }) => {
  if (!plan) return null
  
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      className="bg-gradient-to-r from-primary to-secondary rounded-xl p-6 text-white"
    >
      <h3 className="text-xl font-bold mb-4">Recommended Action Plan</h3>
      
      <div className="space-y-3">
        {plan.steps?.map((step, idx) => (
          <div key={idx} className="flex items-center space-x-3">
            <div className="w-8 h-8 bg-white/20 rounded-full flex items-center justify-center font-bold">
              {idx + 1}
            </div>
            <p>{step}</p>
          </div>
        ))}
      </div>
      
      <div className="mt-6 pt-4 border-t border-white/20">
        <p className="text-sm">
          Expected Impact: <span className="font-bold">{plan.expected_impact}</span>
        </p>
      </div>
    </motion.div>
  )
}

export default ActionPlan