# Admin Dashboard

A modern admin dashboard built with React, TypeScript, and Vite to manage multiple projects including a Quote API and a Blog.

## Features

- **Dashboard Overview**: View key metrics and statistics for all managed projects
- **Quote API Management**: Add, edit, and delete quotes in your quote API
- **Blog Management**: Create, edit, publish, and delete blog posts
- **Authentication**: Secure login system with protected routes
- **Responsive Design**: Works on desktop and mobile devices

## Tech Stack

- **Frontend**: React 19, TypeScript, TailwindCSS
- **State Management**: React Query for server state, React Context for local state
- **Routing**: React Router v7
- **UI Components**: Headless UI and Heroicons
- **HTTP Client**: Axios
- **Build Tool**: Vite

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm, yarn, or pnpm

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/admin-dashboard.git
cd admin-dashboard
```

2. Install dependencies
```bash
npm install
# or
yarn
# or
pnpm install
```

3. Create a `.env` file in the root directory with the following content:
```
VITE_API_BASE_URL=http://localhost:3000/api
```

4. Start the development server
```bash
npm run dev
# or
yarn dev
# or
pnpm dev
```

5. Open your browser and navigate to `http://localhost:5173`

### Login Credentials

For development purposes, you can use the following credentials:
- Email: admin@example.com
- Password: password

## Project Structure

```
admin-dashboard/
├── public/              # Static assets
├── src/
│   ├── assets/          # Images, fonts, etc.
│   ├── components/      # Reusable components
│   ├── context/         # React context providers
│   ├── hooks/           # Custom React hooks
│   ├── layouts/         # Layout components
│   ├── pages/           # Page components
│   ├── services/        # API services
│   ├── types/           # TypeScript type definitions
│   ├── utils/           # Utility functions
│   ├── App.tsx          # Main App component
│   ├── main.tsx         # Entry point
│   └── index.css        # Global styles
├── .env                 # Environment variables
├── index.html           # HTML template
├── package.json         # Project dependencies
├── postcss.config.js    # PostCSS configuration
├── tailwind.config.js   # Tailwind CSS configuration
├── tsconfig.json        # TypeScript configuration
└── vite.config.ts       # Vite configuration
```

## Connecting to External Projects

This admin dashboard is designed to connect to external projects like a Quote API and a Blog. By default, it expects these services to be available at:

- Quote API: `http://localhost:3000/api/quotes`
- Blog API: `http://localhost:3000/api/posts`

You can modify the API endpoints in the `.env` file or in `src/services/api.ts`.

## License

MIT
