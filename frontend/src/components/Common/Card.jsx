import React from 'react'
import { motion } from 'framer-motion'

const Card = ({ children, title, icon, className = '', animate = true }) => {
  const CardContent = (
    <div className={`bg-white dark:bg-gray-800 rounded-xl shadow-lg overflow-hidden ${className}`}>
      {(title || icon) && (
        <div className="px-6 py-4 border-b border-gray-200 dark:border-gray-700">
          <div className="flex items-center space-x-3">
            {icon && <div className="text-2xl">{icon}</div>}
            {title && <h3 className="text-lg font-semibold">{title}</h3>}
          </div>
        </div>
      )}
      <div className="p-6">{children}</div>
    </div>
  )
  
  if (animate) {
    return (
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        {CardContent}
      </motion.div>
    )
  }
  
  return CardContent
}

export default Card