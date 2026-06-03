import { useState, useEffect } from 'react'

export const useAuth = () => {
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (token) {
      // Validate token with backend
      setUser({ name: 'Admin User', email: 'admin@example.com' })
    }
    setLoading(false)
  }, [])

  const login = async (email, password) => {
    // Mock login - replace with actual API call
    localStorage.setItem('token', 'mock-token')
    setUser({ name: 'Admin User', email })
    return true
  }

  const logout = () => {
    localStorage.removeItem('token')
    setUser(null)
  }

  return { user, loading, login, logout }
}