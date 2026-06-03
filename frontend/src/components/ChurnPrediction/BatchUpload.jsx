import React, { useCallback, useState } from 'react'
import { useDropzone } from 'react-dropzone'
import toast from 'react-hot-toast'
import { churnService } from '../../services/churnService'

const BatchUpload = ({ onUploadComplete }) => {
  const [uploading, setUploading] = useState(false)
  const [file, setFile] = useState(null)
  
  const onDrop = useCallback((acceptedFiles) => {
    const uploadedFile = acceptedFiles[0]
    if (uploadedFile && uploadedFile.type === 'text/csv') {
      setFile(uploadedFile)
      toast.success('File uploaded successfully')
    } else {
      toast.error('Please upload a CSV file')
    }
  }, [])
  
  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'text/csv': ['.csv']
    },
    maxFiles: 1
  })
  
  const handleUpload = async () => {
    if (!file) {
      toast.error('Please select a file first')
      return
    }
    
    setUploading(true)
    try {
      const result = await churnService.batchPredict(file)
      toast.success(`Processed ${result.total_customers} customers`)
      onUploadComplete(result)
    } catch (error) {
      toast.error('Upload failed')
    } finally {
      setUploading(false)
    }
  }
  
  return (
    <div className="space-y-4">
      <div
        {...getRootProps()}
        className={`border-2 border-dashed rounded-xl p-8 text-center cursor-pointer transition-all
          ${isDragActive ? 'border-primary bg-primary/10' : 'border-gray-300 dark:border-gray-600'}`}
      >
        <input {...getInputProps()} />
        {isDragActive ? (
          <p className="text-primary">Drop the CSV file here...</p>
        ) : (
          <div>
            <p className="text-gray-600 dark:text-gray-400">Drag & drop a CSV file here</p>
            <p className="text-sm text-gray-500 mt-2">or click to select</p>
          </div>
        )}
      </div>
      
      {file && (
        <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
          <div>
            <p className="font-medium">{file.name}</p>
            <p className="text-sm text-gray-500">{(file.size / 1024).toFixed(2)} KB</p>
          </div>
          <button
            onClick={handleUpload}
            disabled={uploading}
            className="btn-primary"
          >
            {uploading ? 'Uploading...' : 'Upload & Predict'}
          </button>
        </div>
      )}
    </div>
  )
}

export default BatchUpload