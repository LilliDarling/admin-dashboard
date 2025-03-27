import axios from 'axios';

// Create an axios instance with default config
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:3000/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add a request interceptor for authentication
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('auth_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Quote API services
export const quoteService = {
  getQuotes: async () => {
    try {
      const response = await api.get('/quotes');
      return response.data;
    } catch (error) {
      console.error('Error fetching quotes:', error);
      throw error;
    }
  },
  
  addQuote: async (quote: { text: string; author: string; category: string }) => {
    try {
      const response = await api.post('/quotes', quote);
      return response.data;
    } catch (error) {
      console.error('Error adding quote:', error);
      throw error;
    }
  },
  
  deleteQuote: async (id: string) => {
    try {
      const response = await api.delete(`/quotes/${id}`);
      return response.data;
    } catch (error) {
      console.error('Error deleting quote:', error);
      throw error;
    }
  },
};

// Blog services
export const blogService = {
  getPosts: async () => {
    try {
      const response = await api.get('/posts');
      return response.data;
    } catch (error) {
      console.error('Error fetching blog posts:', error);
      throw error;
    }
  },
  
  addPost: async (post: { 
    title: string; 
    excerpt: string; 
    content: string; 
    author: string; 
    status: 'draft' | 'published' 
  }) => {
    try {
      const response = await api.post('/posts', post);
      return response.data;
    } catch (error) {
      console.error('Error adding blog post:', error);
      throw error;
    }
  },
  
  updatePost: async (id: string, post: { 
    title?: string; 
    excerpt?: string; 
    content?: string; 
    author?: string; 
    status?: 'draft' | 'published' 
  }) => {
    try {
      const response = await api.put(`/posts/${id}`, post);
      return response.data;
    } catch (error) {
      console.error('Error updating blog post:', error);
      throw error;
    }
  },
  
  deletePost: async (id: string) => {
    try {
      const response = await api.delete(`/posts/${id}`);
      return response.data;
    } catch (error) {
      console.error('Error deleting blog post:', error);
      throw error;
    }
  },
  
  publishPost: async (id: string) => {
    try {
      const response = await api.patch(`/posts/${id}/publish`);
      return response.data;
    } catch (error) {
      console.error('Error publishing blog post:', error);
      throw error;
    }
  },
};

// Dashboard statistics service
export const statsService = {
  getDashboardStats: async () => {
    try {
      const response = await api.get('/stats/dashboard');
      return response.data;
    } catch (error) {
      console.error('Error fetching dashboard stats:', error);
      throw error;
    }
  },
};

export default api;