import React, { useState } from 'react'

const ROISliders = ({ onSimulate }) => {
  const [params, setParams] = useState({
    numCustomers: 1000,
    successRate: 50,
    discountPercent: 20,
    costPerCustomer: 50
  })
  
  const handleChange = (key, value) => {
    const newParams = { ...params, [key]: value }
    setParams(newParams)
    onSimulate(newParams)
  }
  
  return (
    <div className="space-y-6">
      <div>
        <label className="block text-sm font-medium mb-2">
          Number of Customers to Target: {params.numCustomers}
        </label>
        <input
          type="range"
          min="100"
          max="10000"
          step="100"
          value={params.numCustomers}
          onChange={(e) => handleChange('numCustomers', parseInt(e.target.value))}
          className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium mb-2">
          Expected Success Rate: {params.successRate}%
        </label>
        <input
          type="range"
          min="0"
          max="100"
          value={params.successRate}
          onChange={(e) => handleChange('successRate', parseInt(e.target.value))}
          className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium mb-2">
          Discount Percentage: {params.discountPercent}%
        </label>
        <input
          type="range"
          min="0"
          max="50"
          value={params.discountPercent}
          onChange={(e) => handleChange('discountPercent', parseInt(e.target.value))}
          className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
        />
      </div>
      
      <div>
        <label className="block text-sm font-medium mb-2">
          Cost per Customer: ${params.costPerCustomer}
        </label>
        <input
          type="range"
          min="10"
          max="200"
          step="5"
          value={params.costPerCustomer}
          onChange={(e) => handleChange('costPerCustomer', parseInt(e.target.value))}
          className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer"
        />
      </div>
    </div>
  )
}

export default ROISliders