import React, { useState } from 'react'
import ROISliders from '../components/Simulation/ROISliders'
import SimulationResults from '../components/Simulation/SimulationResults'
import ComparisonChart from '../components/Simulation/ComparisonChart'
import Card from '../components/Common/Card'
import { simulationService } from '../services/simulationService'
import toast from 'react-hot-toast'

const SimulationPage = () => {
  const [simulationResults, setSimulationResults] = useState(null)
  const [comparisonData, setComparisonData] = useState([])
  const [simulating, setSimulating] = useState(false)

  const handleSimulate = async (params) => {
    setSimulating(true)
    try {
      const requestData = {
        strategy: {
          strategy_name: params.strategyName || "Custom Strategy",
          target_segment: params.targetSegment || 0,
          discount_percent: params.discountPercent || 0,
          free_services: params.freeServices || [],
          contract_upgrade_months: params.contractUpgrade || 0,
          priority_support: params.prioritySupport || false,
          cost_per_customer: params.costPerCustomer || 50
        },
        num_customers_to_target: params.numCustomers || 1000,
        expected_success_rate: params.successRate || 50,
        simulation_period_months: params.simulationPeriod || 12
      }
      
      const results = await simulationService.simulateROI(requestData)
      
      setSimulationResults(results)
      
      // Update comparison data
      setComparisonData(prev => {
        const newData = [...prev, {
          name: `Scenario ${prev.length + 1}`,
          roi: results.roi_percentage || 0,
          customers_saved: results.customers_saved || 0
        }]
        return newData.slice(-5)
      })
      
      toast.success('Simulation completed successfully!')
    } catch (error) {
      console.error('Simulation error:', error)
      toast.error(error.response?.data?.detail || 'Simulation failed. Please try again.')
    } finally {
      setSimulating(false)
    }
  }

  const clearScenarios = () => {
    setComparisonData([])
    setSimulationResults(null)
    toast.success('All scenarios cleared!')
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">ROI Simulation</h1>
          <p className="text-gray-600 dark:text-gray-400">Simulate retention strategy ROI before implementation</p>
        </div>
        {comparisonData.length > 0 && (
          <button
            onClick={clearScenarios}
            className="px-4 py-2 text-sm bg-gray-200 dark:bg-gray-700 rounded-lg hover:bg-gray-300 dark:hover:bg-gray-600 transition-colors"
          >
            Clear All Scenarios
          </button>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card title="Simulation Parameters">
          <ROISliders onSimulate={handleSimulate} />
          {simulating && (
            <div className="mt-6 text-center">
              <div className="inline-flex items-center space-x-2 text-gray-600 dark:text-gray-400">
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-primary"></div>
                <span>Calculating ROI...</span>
              </div>
            </div>
          )}
        </Card>

        <Card title="Simulation Results">
          {simulationResults ? (
            <SimulationResults results={simulationResults} />
          ) : (
            <div className="text-center py-12 text-gray-500 dark:text-gray-400">
              <p className="text-6xl mb-4">📊</p>
              <p>Adjust the parameters and click Simulate to see results</p>
            </div>
          )}
        </Card>
      </div>

      {comparisonData.length > 0 && (
        <Card title="Scenario Comparison">
          <ComparisonChart data={comparisonData} />
          <div className="mt-4 text-sm text-gray-500 dark:text-gray-400 text-center">
            Showing last {comparisonData.length} scenarios
          </div>
        </Card>
      )}

      <Card title="Simulation Guide">
        <div className="prose dark:prose-invert max-w-none">
          <h4 className="font-semibold text-gray-900 dark:text-white">How to use ROI Simulation:</h4>
          <ol className="list-decimal list-inside space-y-2 mt-2 text-gray-600 dark:text-gray-400">
            <li>Adjust the number of customers you want to target</li>
            <li>Set expected success rate based on historical data</li>
            <li>Define discount percentage and cost per customer</li>
            <li>Review ROI calculation and breakeven analysis</li>
            <li>Compare multiple scenarios to find optimal strategy</li>
          </ol>
          
          <h4 className="font-semibold text-gray-900 dark:text-white mt-4">Understanding the Metrics:</h4>
          <ul className="list-disc list-inside space-y-1 mt-2 text-gray-600 dark:text-gray-400">
            <li><strong>ROI%</strong> - Return on Investment percentage</li>
            <li><strong>Net Savings</strong> - Total revenue retained minus costs</li>
            <li><strong>Customers Saved</strong> - Estimated customers retained</li>
            <li><strong>Payback Period</strong> - Months to recover investment</li>
          </ul>
          
          <div className="mt-4 p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg border border-blue-200 dark:border-blue-800">
            <p className="text-sm text-blue-800 dark:text-blue-200">
              💡 <strong>Pro Tip:</strong> A positive ROI (&gt;0%) indicates profitable strategy. 
              Aim for ROI above 20% for optimal results. Run multiple scenarios to find the best combination 
              of discount percentage and success rate for your specific segment.
            </p>
          </div>
        </div>
      </Card>
    </div>
  )
}

export default SimulationPage