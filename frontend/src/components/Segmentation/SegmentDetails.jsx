import React from 'react'
import { XMarkIcon } from '@heroicons/react/24/outline'

const SegmentDetails = ({ segment, onClose }) => {
  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50">
      <div className="bg-white dark:bg-gray-800 rounded-xl max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <div className="flex justify-between items-center p-6 border-b border-gray-200 dark:border-gray-700">
          <h2 className="text-2xl font-bold">{segment.segment_name}</h2>
          <button onClick={onClose} className="p-1 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg">
            <XMarkIcon className="h-6 w-6" />
          </button>
        </div>
        
        <div className="p-6 space-y-6">
          <div className="grid grid-cols-2 gap-4">
            <div className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
              <p className="text-sm text-gray-500">Segment Size</p>
              <p className="text-2xl font-bold">{segment.size}</p>
            </div>
            <div className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
              <p className="text-sm text-gray-500">Avg Churn Rate</p>
              <p className="text-2xl font-bold text-danger">{segment.avg_churn_rate}%</p>
            </div>
            <div className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
              <p className="text-sm text-gray-500">Avg Tenure</p>
              <p className="text-2xl font-bold">{segment.avg_tenure} months</p>
            </div>
            <div className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
              <p className="text-sm text-gray-500">Avg Monthly Charges</p>
              <p className="text-2xl font-bold">${segment.avg_monthly_charges}</p>
            </div>
          </div>
          
          <div>
            <h3 className="font-semibold mb-2">Characteristics</h3>
            <p className="text-gray-600 dark:text-gray-400">{segment.characteristics}</p>
          </div>
          
          <div>
            <h3 className="font-semibold mb-2">Recommended Actions</h3>
            <ul className="list-disc list-inside space-y-1 text-gray-600 dark:text-gray-400">
              <li>Targeted retention campaigns</li>
              <li>Personalized offers based on segment behavior</li>
              <li>Monitor churn indicators closely</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

export default SegmentDetails