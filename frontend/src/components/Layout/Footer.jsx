import React from 'react'

const Footer = () => {
  const currentYear = new Date().getFullYear()
  
  return (
    <footer className="bg-white dark:bg-gray-800 shadow-lg mt-auto border-t border-gray-200 dark:border-gray-700">
      <div className="max-w-7xl mx-auto py-4 px-4 sm:px-6 lg:px-8">
        <div className="text-center text-gray-500 dark:text-gray-400 text-sm">
          © {currentYear} Customer Churn Prediction System. All rights reserved.
        </div>
      </div>
    </footer>
  )
}

export default Footer