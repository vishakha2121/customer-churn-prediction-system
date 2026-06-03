import React, { useState } from 'react'

const SegmentFilter = ({ onFilterChange }) => {
  const [filters, setFilters] = useState({
    minTenure: '',
    maxTenure: '',
    minCharges: '',
    maxCharges: '',
    contractType: '',
    paymentMethod: ''
  })
  
  const handleChange = (key, value) => {
    const newFilters = { ...filters, [key]: value }
    setFilters(newFilters)
    onFilterChange(newFilters)
  }
  
  return (
    <div className="bg-white dark:bg-gray-800 rounded-xl shadow-lg p-6">
      <h3 className="text-lg font-semibold mb-4">Filter Segments</h3>
      
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Tenure Range</label>
          <div className="flex space-x-2">
            <input
              type="number"
              placeholder="Min"
              value={filters.minTenure}
              onChange={(e) => handleChange('minTenure', e.target.value)}
              className="input-field"
            />
            <input
              type="number"
              placeholder="Max"
              value={filters.maxTenure}
              onChange={(e) => handleChange('maxTenure', e.target.value)}
              className="input-field"
            />
          </div>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Monthly Charges</label>
          <div className="flex space-x-2">
            <input
              type="number"
              placeholder="Min"
              value={filters.minCharges}
              onChange={(e) => handleChange('minCharges', e.target.value)}
              className="input-field"
            />
            <input
              type="number"
              placeholder="Max"
              value={filters.maxCharges}
              onChange={(e) => handleChange('maxCharges', e.target.value)}
              className="input-field"
            />
          </div>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Contract Type</label>
          <select
            value={filters.contractType}
            onChange={(e) => handleChange('contractType', e.target.value)}
            className="input-field"
          >
            <option value="">All</option>
            <option value="Month-to-month">Month-to-month</option>
            <option value="One year">One year</option>
            <option value="Two year">Two year</option>
          </select>
        </div>
      </div>
    </div>
  )
}

export default SegmentFilter