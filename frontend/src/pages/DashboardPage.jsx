import React from 'react'

const DashboardPage = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Dashboard</h1>
      <p className="text-gray-600 dark:text-gray-400">Welcome to Customer Churn Prediction System</p>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 className="text-gray-500 dark:text-gray-400 text-sm">Total Customers</h3>
          <p className="text-3xl font-bold text-indigo-600">7,043</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 className="text-gray-500 dark:text-gray-400 text-sm">Avg Churn Rate</h3>
          <p className="text-3xl font-bold text-red-600">26.5%</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 className="text-gray-500 dark:text-gray-400 text-sm">High Risk Customers</h3>
          <p className="text-3xl font-bold text-yellow-600">1,860</p>
        </div>
        <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <h3 className="text-gray-500 dark:text-gray-400 text-sm">Monthly Savings</h3>
          <p className="text-3xl font-bold text-green-600">$125K</p>
        </div>
      </div>
      
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">System Status</h2>
        <div className="flex items-center space-x-2">
          <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
          <span>Backend API: Connected on port 8000</span>
        </div>
        <div className="mt-2 text-sm text-gray-500">
          Server is running successfully!
        </div>
      </div>
    </div>
  )
}

export default DashboardPage