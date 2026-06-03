import React, { useState } from 'react'
import { useForm } from 'react-hook-form'
import toast from 'react-hot-toast'
import { churnService } from '../../services/churnService'

const PredictionForm = ({ onPredictionComplete }) => {
  const { register, handleSubmit, formState: { errors } } = useForm()
  const [loading, setLoading] = useState(false)
  
  const onSubmit = async (data) => {
    setLoading(true)
    try {
      const result = await churnService.predictSingle(data)
      toast.success('Prediction completed!')
      onPredictionComplete(result)
    } catch (error) {
      toast.error('Failed to make prediction')
      console.error(error)
    } finally {
      setLoading(false)
    }
  }
  
  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
            Customer ID
          </label>
          <input
            {...register('customer_id', { required: 'Customer ID is required' })}
            className="input-field mt-1"
            placeholder="CUST001"
          />
          {errors.customer_id && <p className="text-red-500 text-sm mt-1">{errors.customer_id.message}</p>}
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
            Tenure (months)
          </label>
          <input
            type="number"
            {...register('tenure_months', { required: true, min: 0, max: 100 })}
            className="input-field mt-1"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
            Monthly Charges ($)
          </label>
          <input
            type="number"
            step="0.01"
            {...register('monthly_charges', { required: true, min: 0 })}
            className="input-field mt-1"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
            Contract Type
          </label>
          <select {...register('contract_type', { required: true })} className="input-field mt-1">
            <option value="Month-to-month">Month-to-month</option>
            <option value="One year">One year</option>
            <option value="Two year">Two year</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
            Payment Method
          </label>
          <select {...register('payment_method', { required: true })} className="input-field mt-1">
            <option value="Electronic check">Electronic check</option>
            <option value="Mailed check">Mailed check</option>
            <option value="Bank transfer">Bank transfer</option>
            <option value="Credit card">Credit card</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300">
            Internet Service
          </label>
          <select {...register('internet_service')} className="input-field mt-1">
            <option value="DSL">DSL</option>
            <option value="Fiber optic">Fiber optic</option>
            <option value="No">No</option>
          </select>
        </div>
      </div>
      
      <div className="flex justify-end">
        <button
          type="submit"
          disabled={loading}
          className="btn-primary flex items-center space-x-2"
        >
          {loading ? (
            <>
              <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white"></div>
              <span>Predicting...</span>
            </>
          ) : (
            <span>Predict Churn Risk</span>
          )}
        </button>
      </div>
    </form>
  )
}

export default PredictionForm