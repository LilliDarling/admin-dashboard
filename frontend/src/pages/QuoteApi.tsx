import { useState, useEffect } from 'react';

interface Quote {
  id: string;
  text: string;
  author: string;
  category: string;
}

export default function QuoteApi() {
  const [quotes, setQuotes] = useState<Quote[]>([]);
  const [newQuote, setNewQuote] = useState<Omit<Quote, 'id'>>({
    text: '',
    author: '',
    category: ''
  });

  // Simulate fetching quotes
  useEffect(() => {
    // In a real app, this would be an API call
    const fetchQuotes = () => {
      // Mock data
      setQuotes([
        {
          id: '1',
          text: 'The best way to predict the future is to invent it.',
          author: 'Alan Kay',
          category: 'Technology'
        },
        {
          id: '2',
          text: 'Innovation distinguishes between a leader and a follower.',
          author: 'Steve Jobs',
          category: 'Business'
        },
        {
          id: '3',
          text: 'The only way to do great work is to love what you do.',
          author: 'Steve Jobs',
          category: 'Motivation'
        }
      ]);
    };

    fetchQuotes();
  }, []);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setNewQuote(prev => ({ ...prev, [name]: value }));
  };

  const handleAddQuote = () => {
    if (!newQuote.text || !newQuote.author || !newQuote.category) {
      alert('Please fill in all fields');
      return;
    }

    // In a real app, this would be an API call
    const newId = (quotes.length + 1).toString();
    const quoteToAdd = { ...newQuote, id: newId };
    
    setQuotes(prev => [...prev, quoteToAdd]);
    setNewQuote({ text: '', author: '', category: '' });
  };

  const handleDeleteQuote = (id: string) => {
    // In a real app, this would be an API call
    setQuotes(prev => prev.filter(quote => quote.id !== id));
  };

  return (
    <div>
      <h1 className="text-2xl font-semibold text-gray-900">Quote API Management</h1>
      
      {/* Add new quote form */}
      <div className="mt-6 bg-white p-6 rounded-lg shadow">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Add New Quote</h2>
        <div className="grid grid-cols-1 gap-y-6 gap-x-4 sm:grid-cols-6">
          <div className="sm:col-span-6">
            <label htmlFor="text" className="block text-sm font-medium text-gray-700">
              Quote Text
            </label>
            <div className="mt-1">
              <input
                type="text"
                name="text"
                id="text"
                value={newQuote.text}
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
                value={newQuote.author}
                onChange={handleInputChange}
                className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              />
            </div>
          </div>

          <div className="sm:col-span-3">
            <label htmlFor="category" className="block text-sm font-medium text-gray-700">
              Category
            </label>
            <div className="mt-1">
              <select
                id="category"
                name="category"
                value={newQuote.category}
                onChange={handleInputChange}
                className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
              >
                <option value="">Select a category</option>
                <option value="Business">Business</option>
                <option value="Motivation">Motivation</option>
                <option value="Technology">Technology</option>
                <option value="Life">Life</option>
                <option value="Success">Success</option>
              </select>
            </div>
          </div>
        </div>
        <div className="mt-6">
          <button
            type="button"
            onClick={handleAddQuote}
            className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Add Quote
          </button>
        </div>
      </div>

      {/* Quotes list */}
      <div className="mt-8">
        <h2 className="text-lg font-medium text-gray-900 mb-4">Quotes</h2>
        <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
          <table className="min-w-full divide-y divide-gray-300">
            <thead className="bg-gray-50">
              <tr>
                <th scope="col" className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">
                  Quote
                </th>
                <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                  Author
                </th>
                <th scope="col" className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                  Category
                </th>
                <th scope="col" className="relative py-3.5 pl-3 pr-4 sm:pr-6">
                  <span className="sr-only">Actions</span>
                </th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-200 bg-white">
              {quotes.map((quote) => (
                <tr key={quote.id}>
                  <td className="whitespace-normal py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">
                    {quote.text}
                  </td>
                  <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{quote.author}</td>
                  <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{quote.category}</td>
                  <td className="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                    <button
                      onClick={() => handleDeleteQuote(quote.id)}
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