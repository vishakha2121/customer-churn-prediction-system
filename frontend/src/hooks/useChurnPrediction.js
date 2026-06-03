import { useState } from 'react'
import { churnService } from '../services/churnService'
import toast from 'react-hot-toast'

export const useChurnPrediction = () => {
  const [prediction, setPrediction] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const predict = async (customerData) => {
    setLoading(true)
    setError(null)
    try {
      const result = await churnService.predictSingle(customerData)
      setPrediction(result)
      return result
    } catch (err) {
      setError(err.message)
      toast.error('Prediction failed')
      throw err
    } finally {
      setLoading(false)
    }
  }

  const reset = () => {
    setPrediction(null)
    setError(null)
  }

  return { prediction, loading, error, predict, reset }
}