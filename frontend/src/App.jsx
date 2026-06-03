import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import Layout from './components/Layout/Layout'
import DashboardPage from './pages/DashboardPage'
import ChurnPredictionPage from './pages/ChurnPredictionPage'

// Simple placeholder components for other pages
const SegmentationPage = () => <div className="p-6"><h1>Segmentation Page</h1></div>
const RetentionStrategiesPage = () => <div className="p-6"><h1>Retention Strategies Page</h1></div>
const SimulationPage = () => <div className="p-6"><h1>Simulation Page</h1></div>
const ReportsPage = () => <div className="p-6"><h1>Reports Page</h1></div>
const SettingsPage = () => <div className="p-6"><h1>Settings Page</h1></div>

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/dashboard" replace />} />
      <Route path="/dashboard" element={<Layout><DashboardPage /></Layout>} />
      <Route path="/churn-prediction" element={<Layout><ChurnPredictionPage /></Layout>} />
      <Route path="/segmentation" element={<Layout><SegmentationPage /></Layout>} />
      <Route path="/retention-strategies" element={<Layout><RetentionStrategiesPage /></Layout>} />
      <Route path="/simulation" element={<Layout><SimulationPage /></Layout>} />
      <Route path="/reports" element={<Layout><ReportsPage /></Layout>} />
      <Route path="/settings" element={<Layout><SettingsPage /></Layout>} />
    </Routes>
  )
}

export default App