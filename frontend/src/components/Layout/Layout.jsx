import React, { useState } from 'react'
import { Link } from 'react-router-dom'

const Layout = ({ children }) => {
  const [sidebarOpen, setSidebarOpen] = useState(true)
  
  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
      {/* Navbar */}
      <nav className="bg-white dark:bg-gray-800 shadow-lg fixed top-0 left-0 right-0 z-50">
        <div className="px-4 py-3 flex justify-between items-center">
          <div className="flex items-center">
            <button 
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className="text-gray-600 dark:text-gray-300 mr-4"
            >
              ☰
            </button>
            <h1 className="text-xl font-bold text-indigo-600">ChurnPredict</h1>
          </div>
          <div className="flex items-center space-x-4">
            <span className="text-gray-600 dark:text-gray-300">Admin</span>
          </div>
        </div>
      </nav>
      
      {/* Sidebar */}
      <aside className={`fixed left-0 top-16 h-full bg-white dark:bg-gray-800 shadow-lg transition-all duration-300 z-40 ${sidebarOpen ? 'w-64' : 'w-16'}`}>
        <nav className="mt-6">
          <Link to="/dashboard" className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            📊 Dashboard
          </Link>
          <Link to="/churn-prediction" className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            🔮 Churn Prediction
          </Link>
          <Link to="/segmentation" className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            📈 Segmentation
          </Link>
          <Link to="/retention-strategies" className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            💎 Retention
          </Link>
          <Link to="/simulation" className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            🎮 Simulation
          </Link>
          <Link to="/reports" className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            📄 Reports
          </Link>
          <Link to="/settings" className="block px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            ⚙️ Settings
          </Link>
        </nav>
      </aside>
      
      {/* Main Content */}
      <main className={`pt-16 transition-all duration-300 ${sidebarOpen ? 'ml-64' : 'ml-16'}`}>
        <div className="p-6">
          {children}
        </div>
      </main>
    </div>
  )
}

export default Layout