import React, { useState } from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Bars3Icon, XMarkIcon, BellIcon, UserCircleIcon, SunIcon, MoonIcon } from '@heroicons/react/24/outline'
import { useTheme } from '../../context/ThemeContext'

const Navbar = ({ sidebarOpen, setSidebarOpen }) => {
  const location = useLocation()
  const { theme, toggleTheme } = useTheme()
  
  const getPageTitle = () => {
    const path = location.pathname
    if (path === '/dashboard') return 'Dashboard'
    if (path === '/churn-prediction') return 'Churn Prediction'
    if (path === '/segmentation') return 'Customer Segmentation'
    if (path === '/retention-strategies') return 'Retention Strategies'
    if (path === '/simulation') return 'ROI Simulation'
    if (path === '/reports') return 'Reports'
    if (path === '/settings') return 'Settings'
    return 'Churn Predict'
  }
  
  return (
    <nav className="bg-white dark:bg-gray-800 shadow-lg fixed top-0 left-0 right-0 z-50">
      <div className="px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex items-center">
            <button
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className="text-gray-500 dark:text-gray-400 hover:text-gray-600 lg:hidden"
            >
              {sidebarOpen ? <XMarkIcon className="h-6 w-6" /> : <Bars3Icon className="h-6 w-6" />}
            </button>
            
            <Link to="/dashboard" className="flex items-center ml-4">
              <div className="bg-gradient-to-r from-primary to-secondary w-8 h-8 rounded-lg flex items-center justify-center">
                <span className="text-white font-bold text-xl">C</span>
              </div>
              <span className="ml-2 text-xl font-bold text-gray-900 dark:text-white hidden md:block">
                ChurnPredict
              </span>
            </Link>
            
            <h1 className="ml-6 text-lg font-semibold text-gray-700 dark:text-gray-300 hidden lg:block">
              {getPageTitle()}
            </h1>
          </div>
          
          <div className="flex items-center space-x-4">
            <button
              onClick={toggleTheme}
              className="p-2 text-gray-500 hover:text-gray-700 dark:text-gray-400 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700"
            >
              {theme === 'dark' ? <SunIcon className="h-5 w-5" /> : <MoonIcon className="h-5 w-5" />}
            </button>
            
            <div className="flex items-center space-x-3">
              <UserCircleIcon className="h-8 w-8 text-gray-500 dark:text-gray-400" />
              <span className="text-sm font-medium text-gray-700 dark:text-gray-300 hidden md:block">
                Admin User
              </span>
            </div>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar