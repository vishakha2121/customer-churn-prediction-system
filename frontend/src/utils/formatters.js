export const formatCurrency = (amount) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(amount)
}

export const formatPercentage = (value) => {
  return `${value.toFixed(1)}%`
}

export const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'short',
    day: 'numeric',
  })
}

export const formatNumber = (num) => {
  return new Intl.NumberFormat().format(num)
}

export const truncateText = (text, length = 50) => {
  if (text.length <= length) return text
  return text.substring(0, length) + '...'
}

export const getRiskColor = (probability) => {
  if (probability >= 70) return '#ef4444'
  if (probability >= 40) return '#f59e0b'
  return '#10b981'
}

export const getRiskLabel = (probability) => {
  if (probability >= 70) return 'High Risk'
  if (probability >= 40) return 'Medium Risk'
  return 'Low Risk'
}