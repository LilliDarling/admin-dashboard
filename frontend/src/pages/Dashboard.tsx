import { useState, useEffect } from 'react';

export default function Dashboard() {
  const [stats, setStats] = useState({
    quoteApiRequests: 0,
    blogPosts: 0,
    blogViews: 0,
    uptime: '100%'
  });

  // Simulate fetching stats
  useEffect(() => {
    // In a real app, this would be an API call
    const fetchStats = () => {
      // Mock data
      setStats({
        quoteApiRequests: 1243,
        blogPosts: 24,
        blogViews: 5678,
        uptime: '99.9%'
      });
    };

    fetchStats();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-semibold text-gray-900">Dashboard</h1>
      <div className="mt-6 grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
        {/* Quote API Requests */}
        <div className="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
          <dt className="truncate text-sm font-medium text-gray-500">Quote API Requests</dt>
          <dd className="mt-1 text-3xl font-semibold tracking-tight text-gray-900">{stats.quoteApiRequests}</dd>
        </div>

        {/* Blog Posts */}
        <div className="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
          <dt className="truncate text-sm font-medium text-gray-500">Blog Posts</dt>
          <dd className="mt-1 text-3xl font-semibold tracking-tight text-gray-900">{stats.blogPosts}</dd>
        </div>

        {/* Blog Views */}
        <div className="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
          <dt className="truncate text-sm font-medium text-gray-500">Blog Views</dt>
          <dd className="mt-1 text-3xl font-semibold tracking-tight text-gray-900">{stats.blogViews}</dd>
        </div>

        {/* Uptime */}
        <div className="overflow-hidden rounded-lg bg-white px-4 py-5 shadow sm:p-6">
          <dt className="truncate text-sm font-medium text-gray-500">Uptime</dt>
          <dd className="mt-1 text-3xl font-semibold tracking-tight text-gray-900">{stats.uptime}</dd>
        </div>
      </div>

      <h2 className="mt-8 text-xl font-semibold text-gray-900">Recent Activity</h2>
      <div className="mt-4 overflow-hidden rounded-lg bg-white shadow">
        <div className="p-6">
          <p className="text-gray-500">No recent activity to display.</p>
        </div>
      </div>
    </div>
  );
}