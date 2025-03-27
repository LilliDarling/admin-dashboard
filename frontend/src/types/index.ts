// User related types
export interface User {
  id: string;
  username: string;
  email: string;
  role: string;
}

export interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

// Quote API related types
export interface Quote {
  id: string;
  text: string;
  author: string;
  category: string;
}

export interface NewQuote {
  text: string;
  author: string;
  category: string;
}

// Blog related types
export interface BlogPost {
  id: string;
  title: string;
  excerpt: string;
  content: string;
  author: string;
  publishedDate: string;
  status: 'draft' | 'published';
}

export interface NewBlogPost {
  title: string;
  excerpt: string;
  content: string;
  author: string;
  status: 'draft' | 'published';
}

export interface UpdateBlogPost {
  title?: string;
  excerpt?: string;
  content?: string;
  author?: string;
  status?: 'draft' | 'published';
}

// Dashboard related types
export interface DashboardStats {
  quoteApiRequests: number;
  blogPosts: number;
  blogViews: number;
  uptime: string;
}