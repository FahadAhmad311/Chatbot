import axios from 'axios';

const API_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Token ${token}`;
  }
  return config;
});

// Error handler
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error.response?.data || error.message);
    return Promise.reject(error);
  }
);

export const authAPI = {
  register: (username: string, email: string, password: string) =>
    api.post('/register/', { username, email, password }),
  
  login: (username: string, password: string) =>
    api.post('/login/', { username, password }),
  
  getProfile: () =>
    api.get('/profile/'),
};

export const chatAPI = {
  sendMessage: (query: string) =>
    api.post('/chat/', { query }),
  
  getHistory: () =>
    api.get('/history/'),
  
  deleteChat: (chatId: number) =>
    api.delete(`/history/${chatId}/`),
};

export default api;
