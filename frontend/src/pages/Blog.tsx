import { useState, useEffect } from 'react';

interface BlogPost {
  id: string;
  title: string;
  excerpt: string;
  content: string;
  author: string;
  publishedDate: string;
  status: 'draft' | 'published';
}

export default function Blog() {
  const [posts, setPosts] = useState<BlogPost[]>([]);
  const [newPost, setNewPost] = useState<Omit<BlogPost, 'id' | 'publishedDate'>>({
    title: '',
    excerpt: '',
    content: '',
    author: '',
    status: 'draft'
  });

  // Simulate fetching blog posts
  useEffect(() => {
    // In a real app, this would be an API call
    const fetchPosts = () => {
      // Mock data
      setPosts([
        {
          id: '1',
          title: 'Getting Started with React',
          excerpt: 'Learn the basics of React and how to build your first component.',
          content: 'This is the full content of the blog post...',
          author: 'Jane Doe',
          publishedDate: '2025-03-15',
          status: 'published'
        },
        {
          id: '2',
          title: 'Advanced TypeScript Patterns',
          excerpt: 'Explore advanced TypeScript patterns for better type safety.',
          content: 'This is the full content of the blog post...',
          author: 'John Smith',
          publishedDate: '2025-03-20',
          status: 'published'
        },
        {
          id: '3',
          title: 'Upcoming Features in JavaScript',
          excerpt: 'A look at the upcoming features in JavaScript and how they will change development.',
          content: 'This is the full content of the blog post...',
          author: 'Jane Doe',
          publishedDate: '2025-03-25',
          status: 'draft'
        }
      ]);
    };

    fetchPosts();
  }, []);

  const handleInputChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setNewPost(prev => ({ ...prev, [name]: value }));
  };

  const handleAddPost = () => {
    if (!newPost.title || !newPost.excerpt || !newPost.content || !newPost.author) {
      alert('Please fill in all required fields');
      return;
    }

    // In a real app, this would be an API call
    const newId = (posts.length + 1).toString();
    const postToAdd = {
      ...newPost,
      id: newId,
      publishedDate: new Date().toISOString().split('T')[0]
    };
    
    setPosts(prev => [...prev, postToAdd]);
    setNewPost({
      title: '',
      excerpt: '',
      content: '',
      author: '',
      status: 'draft'
    });
  };

  const handleDeletePost = (id: string) => {
    // In a real app, this would be an API call
    setPosts(prev => prev.filter(post => post.id !== id));
  };

  const handlePublishPost = (id: string) => {
    // In a real app, this would be an API call
    setPosts(prev =>
      prev.map(post =>
        post.id === id ? { ...post, status: 'published' as const } : post
      )
    );
  };

  return (
    <div>
      <h1 className="text-2xl font-semibold text-gray-900">Blog Management</h1>
      
      {/* Add new blog post form */}
      <div className="mt-6 bg-white p-6 rounded-lg shadow">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Add New Blog Post</h2>
        <div className="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
          <div className="sm:col-span-6">
            <label htmlFor="title" className="block text-sm font-medium text-gray-700">
              Title
            </label>
            <div className="mt-1">
              <input
                type="text"
                name="title"
                id="title"
                value={newPost.title}
                onChange={handleInputChange}
                className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div className="sm:col-span-6">
            <label htmlFor="excerpt" className="block text-sm font-medium text-gray-700">
              Excerpt
            </label>
            <div className="mt-1">
              <input
                type="text"
                name="excerpt"
                id="excerpt"
                value={newPost.excerpt}
                onChange={handleInputChange}
                className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div className="sm:col-span-6">
            <label htmlFor="content" className="block text-sm font-medium text-gray-700">
              Content
            </label>
            <div className="mt-1">
              <textarea
                id="content"
                name="content"
                rows={5}
                value={newPost.content}
                onChange={handleInputChange}
                className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div className="sm:col-span-3">
            <label htmlFor="author" className="block text-sm font-medium text-gray-700">
              Author
            </label>
            <div className="mt-1">
              <input
                type="text"
                name="author"
                id="author"
                value={newPost.author}
                onChange={handleInputChange}
                className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div className="sm:col-span-3">
            <label htmlFor="status" className="block text-sm font-medium text-gray-700">
              Status
            </label>
            <div className="mt-1">
              <select
                id="status"
                name="status"
                value={newPost.status}
                onChange={handleInputChange}
                className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              >
                <option value="draft">Draft</option>
                <option value="published">Published</option>
              </select>
            </div>
          </div>
        </div>
        <div className="mt-6">
          <button
            type="button"
            onClick={handleAddPost}
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Add Blog Post
          </button>
        </div>
      </div>

      {/* Blog posts list */}
      <div className="mt-8">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Blog Posts</h2>
        <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
          <table className="min-w-full divide-y divide-gray-300">
            <thead className="bg-gray-50">
              <tr>
                <th scope="col" className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">
                  Title
                </th>
                <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                  Author
                </th>
                <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                  Date
                </th>
                <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                  Status
                </th>
                <th scope="col" className="relative py-3.5 pl-3 pr-4 sm:pr-6">
                  <span className="sr-only">Actions</span>
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 bg-white">
              {posts.map((post) => (
                <tr key={post.id}>
                  <td className="whitespace-normal py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">
                    <div>
                      <div className="font-medium">{post.title}</div>
                      <div className="text-gray-500 mt-1">{post.excerpt}</div>
                    </div>
                  </td>
                  <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{post.author}</td>
                  <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{post.publishedDate}</td>
                  <td className="whitespace-nowrap px-3 py-4 text-sm">
                    <span className={`inline-flex rounded-full px-2 text-xs font-semibold leading-5 ${
                      post.status === 'published' 
                        ? 'bg-green-100 text-green-800' 
                        : 'bg-yellow-100 text-yellow-800'
                    }`}>
                      {post.status}
                    </span>
                  </td>
                  <td className="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                    {post.status === 'draft' && (
                      <button
                        onClick={() => handlePublishPost(post.id)}
                        className="text-indigo-600 hover:text-indigo-900 mr-4"
                      >
                        Publish
                      </button>
                    )}
                    <button
                      onClick={() => handleDeletePost(post.id)}
                      className="text-red-600 hover:text-red-900"
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}