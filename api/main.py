from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import sys
from loguru import logger
import time
import traceback
from routers import auth, quotes, posts, stats
from utils.database import initialize_database
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logger with more detailed logging
logger.remove()  # Remove default handler
logger.add(
    "logs/api.log",
    rotation="10 MB",
    retention="7 days",
    level="DEBUG",  # More detailed logging
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {name}:{function}:{line} - {message}"
)
logger.add(sys.stderr, level="INFO")  # Also log to console

# Create FastAPI app
app = FastAPI(
    title="Admin Dashboard API",
    description="Backend API for Admin Dashboard",
    version="0.1.0",
    docs_url="/docs",  # Explicitly set docs URL
)

# Configure CORS
origins = [
    "http://localhost:5173",  # Default Vite dev server
    "http://localhost:3000",
    "http://localhost:8000",
    "*",  # Allow all origins for testing
]

# Add custom origins from environment variables
if os.getenv("FRONTEND_URL"):
    origins.append(os.getenv("FRONTEND_URL"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add database connection check middleware
@app.middleware("http")
async def db_connection_middleware(request: Request, call_next):
    # Skip DB check for non-API routes and docs
    if not request.url.path.startswith("/api") or request.url.path.endswith("/health") or \
       request.url.path.startswith("/docs") or request.url.path.startswith("/openapi.json"):
        return await call_next(request)
    
    # Continue with the request if DB is connected
    return await call_next(request)

# Add request timing middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    
    # Log request details
    logger.debug(f"Request started: {request.method} {request.url.path}")
    
    # Process the request
    response = await call_next(request)
    
    # Calculate and log processing time
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"{request.method} {request.url.path} - {process_time:.4f}s")
    
    return response

# Add global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    error_details = traceback.format_exc()
    logger.error(f"Unhandled exception in {request.url.path}: {exc}\n{error_details}")
    
    # Check if it's a database connection error
    if "AutoReconnect" in str(exc) or "ServerSelectionTimeoutError" in str(exc):
        return JSONResponse(
            status_code=503,
            content={
                "message": "Database connection error. Please try again later.",
                "error": "database_connection_error"
            }
        )
    
    # Return a generic error for other exceptions
    return JSONResponse(
        status_code=500,
        content={
            "message": "Internal server error",
            "error": "internal_server_error"
        }
    )


# Include routers
app.include_router(auth.router, tags=["Authentication"])
# app.include_router(quotes.router, prefix="/api/quotes", tags=["Quotes"])
# app.include_router(posts.router, prefix="/api/posts", tags=["Blog Posts"])
# app.include_router(stats.router, prefix="/api/stats", tags=["Statistics"])

@app.get("/")
async def root():
    """Root endpoint for API health check."""
    return {
        "message": "Welcome to the Admin Dashboard API",
        "version": "0.1.0",
        "status": "active"
    }
