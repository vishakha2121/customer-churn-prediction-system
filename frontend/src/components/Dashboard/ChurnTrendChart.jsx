import React from 'react'
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts'

const ChurnTrendChart = ({ data }) => {
  return (
    <ResponsiveContainer width="100%" height={400}>
      <LineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="churn_rate" stroke="#8884d8" name="Churn Rate %" />
        <Line type="monotone" dataKey="target" stroke="#82ca9d" name="Target %" />
      </LineChart>
    </ResponsiveContainer>
  )
}

export default ChurnTrendChart