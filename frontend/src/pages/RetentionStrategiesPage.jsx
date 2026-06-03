import React, { useState, useEffect } from 'react'
import StrategyCard from '../components/Retention/StrategyCard'
import OfferGenerator from '../components/Retention/OfferGenerator'
import ActionPlan from '../components/Retention/ActionPlan'
import Card from '../components/Common/Card'
import { retentionService } from '../services/retentionService'
import toast from 'react-hot-toast'

const RetentionStrategiesPage = () => {
  const [selectedSegment, setSelectedSegment] = useState(0)
  const [strategies, setStrategies] = useState([])
  const [actionPlan, setActionPlan] = useState(null)
  const [loading, setLoading] = useState(false)

  const segments = [
    { id: 0, name: 'High-Risk Customers' },
    { id: 1, name: 'Premium Loyal' },
    { id: 2, name: 'Value Seekers' },
    { id: 3, name: 'New Customers' }
  ]

  useEffect(() => {
    loadStrategies()
  }, [selectedSegment])

  const loadStrategies = async () => {
    setLoading(true)
    try {
      const data = await retentionService.getStrategies(selectedSegment)
      setStrategies(data.strategies)
    } catch (error) {
      toast.error('Failed to load strategies')
    } finally {
      setLoading(false)
    }
  }

  const handleApplyStrategy = (strategy) => {
    setActionPlan({
      steps: [
        `Launch ${strategy.strategy_name} campaign for target segment`,
        `Send personalized ${strategy.discount}% discount offers`,
        `Assign priority support for affected customers`,
        `Track engagement and conversion metrics`
      ],
      expected_impact: `Expected to retain ${strategy.estimated_success}% of targeted customers`
    })
    toast.success(`Strategy "${strategy.strategy_name}" applied successfully!`)
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Retention Strategies</h1>
        <p className="text-gray-600 dark:text-gray-400">AI-powered retention strategy recommendations</p>
      </div>

      <div className="flex space-x-4 overflow-x-auto pb-4">
        {segments.map(segment => (
          <button
            key={segment.id}
            onClick={() => setSelectedSegment(segment.id)}
            className={`px-6 py-2 rounded-lg font-medium transition-all whitespace-nowrap ${
              selectedSegment === segment.id
                ? 'bg-primary text-white shadow-lg'
                : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-300 dark:hover:bg-gray-600'
            }`}
          >
            {segment.name}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div className="lg:col-span-2">
          <Card title="Recommended Strategies">
            {loading ? (
              <div className="text-center py-10">Loading strategies...</div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                {strategies.map((strategy, idx) => (
                  <StrategyCard
                    key={idx}
                    strategy={strategy}
                    onApply={handleApplyStrategy}
                  />
                ))}
              </div>
            )}
          </Card>
        </div>

        <div className="space-y-6">
          <Card title="Generate Custom Offers">
            <OfferGenerator
              segmentId={selectedSegment}
              onOfferGenerated={() => loadStrategies()}
            />
          </Card>

          {actionPlan && <ActionPlan plan={actionPlan} />}
        </div>
      </div>
    </div>
  )
}

export default RetentionStrategiesPage