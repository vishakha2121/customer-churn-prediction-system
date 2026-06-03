import React from 'react'

const Button = ({ children, variant = 'primary', size = 'md', loading = false, onClick, className = '', ...props }) => {
  const variants = {
    primary: 'bg-primary hover:bg-primary/90 text-white',
    secondary: 'bg-secondary hover:bg-secondary/90 text-white',
    danger: 'bg-danger hover:bg-danger/90 text-white',
    success: 'bg-success hover:bg-success/90 text-white',
    outline: 'border-2 border-primary text-primary hover:bg-primary hover:text-white'
  }
  
  const sizes = {
    sm: 'px-3 py-1 text-sm',
    md: 'px-6 py-2',
    lg: 'px-8 py-3 text-lg'
  }
  
  return (
    <button
      onClick={onClick}
      disabled={loading}
      className={`${variants[variant]} ${sizes[size]} rounded-lg font-medium transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed ${className}`}
      {...props}
    >
      {loading ? (
        <div className="flex items-center justify-center space-x-2">
          <div className="animate-spin rounded-full h-4 w-4 border-b-2 border-white"></div>
          <span>Loading...</span>
        </div>
      ) : (
        children
      )}
    </button>
  )
}

export default Button