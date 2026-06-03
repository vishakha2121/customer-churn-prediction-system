import React from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'

const HomePage = () => {
  return (
    <div className="min-h-screen bg-gradient-to-br from-primary to-secondary">
      <div className="container mx-auto px-4 py-20">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center text-white"
        >
          <h1 className="text-5xl md:text-7xl font-bold mb-6">
            Customer Churn Prediction
          </h1>
          <p className="text-xl md:text-2xl mb-8 opacity-90">
            AI-Powered Retention Optimization System
          </p>
          <Link to="/dashboard" className="inline-block bg-white text-primary px-8 py-3 rounded-lg font-semibold hover:shadow-lg transition-all">
            Get Started
          </Link>
        </motion.div>
      </div>
    </div>
  )
}

export default HomePage