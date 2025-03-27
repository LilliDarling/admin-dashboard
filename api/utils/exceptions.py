from fastapi import HTTPException, status
from loguru import logger
import traceback

async def handle_pymongo_error(error):
    """
    Handle MongoDB errors and raise appropriate HTTP exceptions
    """
    error_str = str(error)
    error_details = traceback.format_exc()
    
    # Log the error
    logger.error(f"MongoDB error: {error}\n{error_details}")
    
    # Check for specific error types
    if "duplicate key error" in error_str:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A resource with this identifier already exists"
        )
    elif "AutoReconnect" in error_str or "ServerSelectionTimeoutError" in error_str:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection error. Please try again later."
        )
    else:
        # Generic database error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database operation failed. Please try again later."
        )

async def handle_not_found_error(resource_type: str):
    """
    Handle not found errors
    """
    logger.info(f"{resource_type} not found")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{resource_type} not found"
    )