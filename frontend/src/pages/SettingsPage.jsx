import React, { useState } from 'react'
import Card from '../components/Common/Card'
import Button from '../components/Common/Button'
import toast from 'react-hot-toast'
import { useTheme } from '../context/ThemeContext'

const SettingsPage = () => {
  const { theme, toggleTheme } = useTheme()
  const [settings, setSettings] = useState({
    emailNotifications: true,
    autoRetention: false,
    alertThreshold: 70,
    reportFrequency: 'weekly',
    apiEndpoint: 'http://localhost:8000/api'
  })

  const handleChange = (key, value) => {
    setSettings({ ...settings, [key]: value })
  }

  const saveSettings = () => {
    localStorage.setItem('appSettings', JSON.stringify(settings))
    toast.success('Settings saved successfully!')
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Settings</h1>
        <p className="text-gray-600 dark:text-gray-400">Manage your application preferences</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card title="General Settings">
          <div className="space-y-4">
            <div className="flex justify-between items-center">
              <div>
                <label className="font-medium">Dark Mode</label>
                <p className="text-sm text-gray-500 dark:text-gray-400">Toggle dark/light theme</p>
              </div>
              <button
                onClick={toggleTheme}
                className="relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
                style={{ backgroundColor: theme === 'dark' ? '#6366f1' : '#d1d5db' }}
              >
                <span
                  className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${
                    theme === 'dark' ? 'translate-x-6' : 'translate-x-1'
                  }`}
                />
              </button>
            </div>

            <div className="flex justify-between items-center">
              <div>
                <label className="font-medium">Email Notifications</label>
                <p className="text-sm text-gray-500 dark:text-gray-400">Receive churn alerts via email</p>
              </div>
              <input
                type="checkbox"
                checked={settings.emailNotifications}
                onChange={(e) => handleChange('emailNotifications', e.target.checked)}
                className="toggle toggle-primary"
              />
            </div>

            <div className="flex justify-between items-center">
              <div>
                <label className="font-medium">Auto-Retention Campaigns</label>
                <p className="text-sm text-gray-500 dark:text-gray-400">Automatically apply retention strategies</p>
              </div>
              <input
                type="checkbox"
                checked={settings.autoRetention}
                onChange={(e) => handleChange('autoRetention', e.target.checked)}
                className="toggle toggle-primary"
              />
            </div>
          </div>
        </Card>

        <Card title="Alert Configuration">
          <div className="space-y-4">
            <div>
              <label className="block font-medium mb-2">Churn Alert Threshold (%)</label>
              <input
                type="range"
                min="0"
                max="100"
                value={settings.alertThreshold}
                onChange={(e) => handleChange('alertThreshold', parseInt(e.target.value))}
                className="w-full"
              />
              <p className="text-sm text-gray-500 mt-1">Alert when churn probability exceeds {settings.alertThreshold}%</p>
            </div>

            <div>
              <label className="block font-medium mb-2">Report Frequency</label>
              <select
                value={settings.reportFrequency}
                onChange={(e) => handleChange('reportFrequency', e.target.value)}
                className="input-field"
              >
                <option value="daily">Daily</option>
                <option value="weekly">Weekly</option>
                <option value="monthly">Monthly</option>
              </select>
            </div>

            <div>
              <label className="block font-medium mb-2">API Endpoint</label>
              <input
                type="text"
                value={settings.apiEndpoint}
                onChange={(e) => handleChange('apiEndpoint', e.target.value)}
                className="input-field"
              />
            </div>
          </div>
        </Card>

        <Card title="Model Configuration">
          <div className="space-y-3">
            <div className="flex justify-between">
              <span>Current Model:</span>
              <span className="font-semibold">Random Forest v2.1</span>
            </div>
            <div className="flex justify-between">
              <span>Last Trained:</span>
              <span>2024-01-15</span>
            </div>
            <div className="flex justify-between">
              <span>Model Accuracy:</span>
              <span className="text-success">85.7%</span>
            </div>
            <Button onClick={() => toast.success('Model retraining started!')}>
              Retrain Model
            </Button>
          </div>
        </Card>

        <Card title="System Status">
          <div className="space-y-3">
            <div className="flex items-center space-x-2">
              <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <span>API Server: <span className="font-semibold">Connected</span></span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <span>Database: <span className="font-semibold">Healthy</span></span>
            </div>
            <div className="flex items-center space-x-2">
              <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <span>ML Models: <span className="font-semibold">Loaded</span></span>
            </div>
            <hr className="my-2" />
            <p className="text-sm text-gray-500">Version: 1.0.0 | Uptime: 99.9%</p>
          </div>
        </Card>
      </div>

      <div className="flex justify-end space-x-4">
        <Button variant="outline" onClick={() => window.location.reload()}>
          Cancel
        </Button>
        <Button onClick={saveSettings}>
          Save Settings
        </Button>
      </div>
    </div>
  )
}

export default SettingsPage