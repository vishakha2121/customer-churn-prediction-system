import React, { useEffect } from 'react'
import { 
  CheckCircleIcon, 
  XCircleIcon, 
  InformationCircleIcon, 
  ExclamationTriangleIcon,
  XMarkIcon
} from '@heroicons/react/24/outline'

const Toast = ({ type, message, onClose, duration = 5000 }) => {
  const types = {
    success: { 
      icon: CheckCircleIcon, 
      color: 'text-green-500', 
      bg: 'bg-green-50 dark:bg-green-900/20',
      border: 'border-green-200 dark:border-green-800'
    },
    error: { 
      icon: XCircleIcon, 
      color: 'text-red-500', 
      bg: 'bg-red-50 dark:bg-red-900/20',
      border: 'border-red-200 dark:border-red-800'
    },
    info: { 
      icon: InformationCircleIcon, 
      color: 'text-blue-500', 
      bg: 'bg-blue-50 dark:bg-blue-900/20',
      border: 'border-blue-200 dark:border-blue-800'
    },
    warning: { 
      icon: ExclamationTriangleIcon, 
      color: 'text-yellow-500', 
      bg: 'bg-yellow-50 dark:bg-yellow-900/20',
      border: 'border-yellow-200 dark:border-yellow-800'
    }
  }
  
  const TypeIcon = types[type]?.icon || types.info.icon
  const styles = types[type] || types.info
  
  useEffect(() => {
    const timer = setTimeout(() => {
      onClose()
    }, duration)
    
    return () => clearTimeout(timer)
  }, [duration, onClose])
  
  return (
    <div className={`${styles.bg} ${styles.border} border rounded-lg shadow-lg p-4 min-w-[300px] max-w-md animate-slide-in`}>
      <div className="flex items-start space-x-3">
        <TypeIcon className={`h-5 w-5 ${styles.color} mt-0.5 flex-shrink-0`} />
        <div className="flex-1">
          <p className="text-sm font-medium text-gray-900 dark:text-white">{message}</p>
        </div>
        <button 
          onClick={onClose} 
          className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-300 flex-shrink-0"
        >
          <XMarkIcon className="h-4 w-4" />
        </button>
      </div>
    </div>
  )
}

export default Toast