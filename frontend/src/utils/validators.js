export const validateEmail = (email) => {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return regex.test(email)
}

export const validatePhone = (phone) => {
  const regex = /^\+?[\d\s-]{10,}$/
  return regex.test(phone)
}

export const validateCustomerData = (data) => {
  const errors = []
  
  if (!data.customer_id) {
    errors.push('Customer ID is required')
  }
  
  if (data.tenure_months < 0 || data.tenure_months > 100) {
    errors.push('Tenure must be between 0 and 100 months')
  }
  
  if (data.monthly_charges < 0 || data.monthly_charges > 1000) {
    errors.push('Monthly charges must be between 0 and 1000')
  }
  
  return {
    isValid: errors.length === 0,
    errors
  }
}

export const validateCSVFile = (file) => {
  if (!file) {
    return { isValid: false, error: 'No file selected' }
  }
  
  if (file.type !== 'text/csv' && !file.name.endsWith('.csv')) {
    return { isValid: false, error: 'File must be CSV format' }
  }
  
  if (file.size > 10 * 1024 * 1024) {
    return { isValid: false, error: 'File size must be less than 10MB' }
  }
  
  return { isValid: true, error: null }
}