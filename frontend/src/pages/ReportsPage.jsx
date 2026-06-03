import React, { useState, useEffect } from 'react'
import Card from '../components/Common/Card'
import { dashboardService } from '../services/api'
import { saveAs } from 'file-saver'
import toast from 'react-hot-toast'

const ReportsPage = () => {
  const [reportData, setReportData] = useState(null)
  const [dateRange, setDateRange] = useState('30')
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    generateReport()
  }, [dateRange])

  const generateReport = async () => {
    setLoading(true)
    try {
      const [kpis, trend] = await Promise.all([
        dashboardService.getKPIs(),
        dashboardService.getChurnTrend()
      ])
      setReportData({ kpis, trend })
    } catch (error) {
      toast.error('Failed to generate report')
    } finally {
      setLoading(false)
    }
  }

  const exportCSV = () => {
    if (!reportData) return
    
    const csvData = [
      ['Metric', 'Value'],
      ['Total Customers', reportData.kpis.total_customers],
      ['Average Churn Rate', `${reportData.kpis.avg_churn_rate}%`],
      ['High Risk Customers', reportData.kpis.high_risk_customers],
      ['Monthly Savings', `$${reportData.kpis.monthly_savings}`],
      ['ROI Percentage', `${reportData.kpis.roi_percentage}%`]
    ]
    
    const csvContent = csvData.map(row => row.join(',')).join('\n')
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8' })
    saveAs(blob, `churn_report_${new Date().toISOString().split('T')[0]}.csv`)
    toast.success('Report exported successfully')
  }

  const exportPDF = () => {
    toast.success('PDF export feature coming soon!')
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Reports & Analytics</h1>
          <p className="text-gray-600 dark:text-gray-400">Generate and export performance reports</p>
        </div>
        <div className="flex space-x-3">
          <button onClick={exportCSV} className="btn-primary">Export CSV</button>
          <button onClick={exportPDF} className="btn-secondary">Export PDF</button>
        </div>
      </div>

      <div className="flex space-x-4">
        <select
          value={dateRange}
          onChange={(e) => setDateRange(e.target.value)}
          className="input-field w-48"
        >
          <option value="7">Last 7 days</option>
          <option value="30">Last 30 days</option>
          <option value="90">Last 90 days</option>
          <option value="365">Last year</option>
        </select>
      </div>

      {loading ? (
        <div className="text-center py-20">Generating report...</div>
      ) : reportData ? (
        <>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <Card title="Executive Summary">
              <div className="space-y-3">
                <p className="text-3xl font-bold text-primary">{reportData.kpis.total_customers?.toLocaleString()}</p>
                <p className="text-gray-600 dark:text-gray-400">Total Active Customers</p>
                <hr className="my-3" />
                <p className="text-2xl font-semibold text-danger">{reportData.kpis.avg_churn_rate}%</p>
                <p className="text-gray-600 dark:text-gray-400">Average Churn Rate</p>
              </div>
            </Card>

            <Card title="Financial Impact">
              <div className="space-y-3">
                <p className="text-2xl font-bold text-success">${reportData.kpis.monthly_savings?.toLocaleString()}</p>
                <p className="text-gray-600 dark:text-gray-400">Monthly Savings</p>
                <p className="text-2xl font-bold text-primary">{reportData.kpis.roi_percentage}%</p>
                <p className="text-gray-600 dark:text-gray-400">ROI</p>
              </div>
            </Card>

            <Card title="Risk Distribution">
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span>High Risk:</span>
                  <span className="font-bold text-danger">{reportData.kpis.high_risk_customers}</span>
                </div>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div 
                    className="bg-danger h-2 rounded-full" 
                    style={{ width: `${(reportData.kpis.high_risk_customers / reportData.kpis.total_customers) * 100}%` }}
                  ></div>
                </div>
              </div>
            </Card>
          </div>

          <Card title="Key Insights">
            <div className="space-y-4">
              <div className="p-4 bg-yellow-50 dark:bg-yellow-900/20 rounded-lg">
                <h4 className="font-semibold text-yellow-800 dark:text-yellow-200">Churn Alert</h4>
                <p className="text-sm text-yellow-700 dark:text-yellow-300 mt-1">
                  High-risk segment increased by 15% this quarter. Immediate retention campaigns recommended.
                </p>
              </div>
              <div className="p-4 bg-green-50 dark:bg-green-900/20 rounded-lg">
                <h4 className="font-semibold text-green-800 dark:text-green-200">Success Story</h4>
                <p className="text-sm text-green-700 dark:text-green-300 mt-1">
                  Retention strategies saved 450 customers this month, generating $125K in retained revenue.
                </p>
              </div>
              <div className="p-4 bg-blue-50 dark:bg-blue-900/20 rounded-lg">
                <h4 className="font-semibold text-blue-800 dark:text-blue-200">Recommendation</h4>
                <p className="text-sm text-blue-700 dark:text-blue-300 mt-1">
                  Increase budget for premium segment loyalty program to maximize ROI.
                </p>
              </div>
            </div>
          </Card>
        </>
      ) : null}
    </div>
  )
}

export default ReportsPage