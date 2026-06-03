import React, { useState, useEffect } from 'react'
import { segmentationService } from '../../services/segmentationService'
import { motion } from 'framer-motion'

const SegmentViewer = () => {
  const [segments, setSegments] = useState([])
  const [selectedSegment, setSelectedSegment] = useState(null)
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    loadSegments()
  }, [])
  
  const loadSegments = async () => {
    try {
      const data = await segmentationService.getSegments()
      setSegments(data.segments)
    } catch (error) {
      console.error('Failed to load segments:', error)
    } finally {
      setLoading(false)
    }
  }
  
  const getSegmentColor = (index) => {
    const colors = ['#6366f1', '#8b5cf6', '#ec4899', '#f59e0b', '#10b981']
    return colors[index % colors.length]
  }
  
  if (loading) return <div className="text-center py-10">Loading segments...</div>
  
  return (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {segments.map((segment, idx) => (
          <motion.div
            key={segment.segment_id}
            whileHover={{ scale: 1.02 }}
            onClick={() => setSelectedSegment(segment)}
            className="cursor-pointer bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6 hover:shadow-xl transition-all"
          >
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold">{segment.segment_name}</h3>
              <div 
                className="w-4 h-4 rounded-full"
                style={{ backgroundColor: getSegmentColor(idx) }}
              ></div>
            </div>
            <p className="text-2xl font-bold text-primary">{segment.size}</p>
            <p className="text-sm text-gray-500 dark:text-gray-400">Customers</p>
            <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
              <p className="text-sm">Churn Rate: <span className="font-semibold">{segment.avg_churn_rate}%</span></p>
              <p className="text-sm mt-1">Avg Tenure: <span className="font-semibold">{segment.avg_tenure} months</span></p>
            </div>
          </motion.div>
        ))}
      </div>
      
      {selectedSegment && (
        <SegmentDetails segment={selectedSegment} onClose={() => setSelectedSegment(null)} />
      )}
    </div>
  )
}

export default SegmentViewer