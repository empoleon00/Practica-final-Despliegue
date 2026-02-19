import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

const api = axios.create({
  baseURL: API_URL,
  timeout: 10000,
})

export const apiService = {
  async getStatus() {
    try {
      const response = await api.get('/')
      return response.data
    } catch (error) {
      console.error('Error fetching status:', error)
      throw error
    }
  },

  async getData() {
    try {
      const response = await api.get('/api/data')
      return response.data
    } catch (error) {
      console.error('Error fetching data:', error)
      throw error
    }
  },
}

export default api

export function setAuthToken(token: string | null) {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`
  } else {
    delete api.defaults.headers.common['Authorization']
  }
}
