import React from 'react'
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const ComparisonChart = ({ data }) => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <BarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar dataKey="roi" fill="#6366f1" name="ROI %" />
        <Bar dataKey="customers_saved" fill="#8b5cf6" name="Customers Saved" />
      </BarChart>
    </ResponsiveContainer>
  )
}

export default ComparisonChart