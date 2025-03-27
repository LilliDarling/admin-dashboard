import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import ProtectedRoute from './components/ProtectedRoute';
import DashboardLayout from './layouts/DashboardLayout';
import Dashboard from './pages/Dashboard';
import QuoteApi from './pages/QuoteApi';
import Blog from './pages/Blog';
import Login from './pages/Login';

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/" element={
            <ProtectedRoute>
              <DashboardLayout>
                <Dashboard />
              </DashboardLayout>
            </ProtectedRoute>
          } />
          <Route path="/quote-api" element={
            <ProtectedRoute>
              <DashboardLayout>
                <QuoteApi />
              </DashboardLayout>
            </ProtectedRoute>
          } />
          <Route path="/blog" element={
            <ProtectedRoute>
              <DashboardLayout>
                <Blog />
              </DashboardLayout>
            </ProtectedRoute>
          } />
        </Routes>
      </Router>
    </AuthProvider>
  );
}

export default App;
