import React, { useState } from 'react'
import SegmentViewer from '../components/Segmentation/SegmentViewer'
import SegmentFilter from '../components/Segmentation/SegmentFilter'
import Card from '../components/Common/Card'

const SegmentationPage = () => {
  const [filters, setFilters] = useState({})

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Customer Segmentation</h1>
        <p className="text-gray-600 dark:text-gray-400">K-Means clustering based customer segments analysis</p>
      </div>

      <SegmentFilter onFilterChange={setFilters} />
      
      <Card>
        <SegmentViewer filters={filters} />
      </Card>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card title="Segment Insights">
          <div className="space-y-4">
            <div className="p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
              <h4 className="font-semibold text-blue-800 dark:text-blue-200">High-Risk Segment</h4>
              <p className="text-sm text-blue-600 dark:text-blue-300 mt-1">
                Customers with month-to-month contracts and high monthly charges show 68% churn probability.
                Focus retention efforts on this segment.
              </p>
            </div>
            <div className="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
              <h4 className="font-semibold text-green-800 dark:text-green-200">Premium Loyal Segment</h4>
              <p className="text-sm text-green-600 dark:text-green-300 mt-1">
                Long-term customers with multiple services. Reward loyalty to maintain high retention.
              </p>
            </div>
          </div>
        </Card>

        <Card title="Recommendations">
          <ul className="space-y-3">
            <li className="flex items-start space-x-3">
              <span className="text-primary">🎯</span>
              <span>Target high-risk segment with personalized discount offers</span>
            </li>
            <li className="flex items-start space-x-3">
              <span className="text-primary">📊</span>
              <span>Launch loyalty program for premium segment</span>
            </li>
            <li className="flex items-start space-x-3">
              <span className="text-primary">🔄</span>
              <span>Implement automated retention campaigns based on segment behavior</span>
            </li>
          </ul>
        </Card>
      </div>
    </div>
  )
}

export default SegmentationPage