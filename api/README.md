# Admin Dashboard Backend

A FastAPI backend for the Admin Dashboard application, providing APIs for authentication, quotes management, blog posts management, and dashboard statistics.

## Features

- User authentication with JWT tokens
- CRUD operations for quotes
- CRUD operations for blog posts
- Dashboard statistics

## Tech Stack

- FastAPI: Modern, fast web framework for building APIs
- MongoDB: NoSQL database
- ODMantic: Async ODM for MongoDB with FastAPI
- Motor: Async MongoDB driver
- Pydantic: Data validation and settings management
- Poetry: Dependency management

## Prerequisites

- Python 3.8 or higher
- Poetry
- MongoDB (local or Atlas)

## Installation

1. Clone the repository
2. Navigate to the backend directory:
   ```
   cd backend
   ```
3. Install dependencies using Poetry:
   ```
   poetry install
   ```
4. Create a `.env` file based on the provided example:
   ```
   # Database
   MONGODB_URL=mongodb://localhost:27017
   DATABASE_NAME=admin_dashboard

   # Authentication
   SECRET_KEY=your-secret-key-for-development-change-in-production
   ACCESS_TOKEN_EXPIRE_MINUTES=30

   # Server
   PORT=3000
   HOST=0.0.0.0
   ```

## Running the Server

1. Make sure MongoDB is running
2. Activate the Poetry virtual environment:
   ```
   poetry shell
   ```
3. Run the server:
   ```
   python run.py
   ```
   
   Or directly with Poetry:
   ```
   poetry run python run.py
   ```

The server will start at http://localhost:3000 by default.

## API Documentation

Once the server is running, you can access the API documentation at:

- Swagger UI: http://localhost:3000/docs
- ReDoc: http://localhost:3000/redoc

## API Endpoints

### Authentication

- `POST /api/auth/register`: Register a new user
- `POST /api/auth/login`: Login and get access token
- `POST /api/auth/token`: Get access token (OAuth2 compatible)

### Quotes

- `GET /api/quotes/`: Get all quotes
- `GET /api/quotes/{quote_id}`: Get a specific quote
- `POST /api/quotes/`: Create a new quote (admin only)
- `PUT /api/quotes/{quote_id}`: Update a quote (admin only)
- `DELETE /api/quotes/{quote_id}`: Delete a quote (admin only)

### Blog Posts

- `GET /api/posts/`: Get all blog posts
- `GET /api/posts/{post_id}`: Get a specific blog post
- `POST /api/posts/`: Create a new blog post (admin only)
- `PUT /api/posts/{post_id}`: Update a blog post (admin only)
- `DELETE /api/posts/{post_id}`: Delete a blog post (admin only)
- `PATCH /api/posts/{post_id}/publish`: Publish a blog post (admin only)

### Statistics

- `GET /api/stats/dashboard`: Get dashboard statistics (admin only)

## Health Check

- `GET /api/health`: Check if the API is running