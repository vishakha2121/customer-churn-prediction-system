import React from 'react'
import { NavLink } from 'react-router-dom'
import { 
  HomeIcon, 
  ChartBarIcon, 
  UserGroupIcon, 
  GiftIcon, 
  BeakerIcon,
  DocumentReportIcon,
  CogIcon
} from '@heroicons/react/24/outline'

const Sidebar = ({ isOpen }) => {
  const menuItems = [
    { path: '/dashboard', name: 'Dashboard', icon: <HomeIcon className="h-5 w-5" /> },
    { path: '/churn-prediction', name: 'Churn Prediction', icon: <ChartBarIcon className="h-5 w-5" /> },
    { path: '/segmentation', name: 'Segmentation', icon: <UserGroupIcon className="h-5 w-5" /> },
    { path: '/retention-strategies', name: 'Retention Strategies', icon: <GiftIcon className="h-5 w-5" /> },
    { path: '/simulation', name: 'ROI Simulation', icon: <BeakerIcon className="h-5 w-5" /> },
    { path: '/reports', name: 'Reports', icon: <DocumentReportIcon className="h-5 w-5" /> },
    { path: '/settings', name: 'Settings', icon: <CogIcon className="h-5 w-5" /> },
  ]
  
  return (
    <aside className={`fixed left-0 top-16 h-full bg-white dark:bg-gray-800 shadow-lg transition-all duration-300 z-40
      ${isOpen ? 'w-64' : 'w-20'} overflow-y-auto`}>
      <nav className="mt-6">
        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) => `
              flex items-center px-6 py-3 mx-2 my-1 rounded-lg transition-all duration-200
              ${isActive 
                ? 'bg-primary text-white shadow-md' 
                : 'text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700'}
              ${!isOpen ? 'justify-center' : ''}
            `}
            title={!isOpen ? item.name : ''}
          >
            <div className="min-w-[24px]">{item.icon}</div>
            <span className={`ml-3 transition-opacity duration-300 ${isOpen ? 'opacity-100' : 'opacity-0 hidden'}`}>
              {item.name}
            </span>
          </NavLink>
        ))}
      </nav>
    </aside>
  )
}

export default Sidebar