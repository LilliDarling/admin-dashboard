from utils.authentication import hash_password
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from auth.utils import verify_password, get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from models.user import UserRequest, UserResponse, Token, LoginRequest
from queries.user import UserQueries
from loguru import logger
import traceback

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

@router.post("/register")
async def register(
    user: UserRequest,
    queries: UserQueries = Depends()
) -> dict: 
    try:
        hashed_password = hash_password(user.password)
        user_new = await queries.create_user(UserRequest(
            username=user.username,
            name=user.name,
            email=user.email,
            password=hashed_password,
        ))
        
        if not user_new:
            # Check if it's because the email is already registered
            existing_email = await UserQueries.get_user_by_email(user.email)
            if existing_email:
                raise HTTPException(status_code=400, detail="Email already registered")
            
            # Check if it's because the username is already taken
            existing_username = await UserQueries.get_user_by_username(user.username)
            if existing_username:
                raise HTTPException(status_code=400, detail="Username already taken")
            
            # If it's neither, it's a server error
            raise HTTPException(
                status_code=500,
                detail="Failed to create user account. Please try again later."
            )
        
        # Log successful registration
        logger.info(f"New user registered successfully: {user.username} ({user.email})")
        
        return {
            "user": UserResponse.from_mongo(user_new)
        }
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log unexpected errors
        error_details = traceback.format_exc()
        logger.error(f"Unexpected error during user registration: {e}\n{error_details}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred. Please try again later."
        )

@router.post("/token", response_model=Token)
async def login_for_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    # Log the token request
    logger.info(f"Token request for username: {form_data.username} from {request.client.host}")
    
    try:
        
        # Authenticate user
        logger.debug(f"Authenticating user: {form_data.username}")
        user = await UserQueries.get_user_by_email(form_data.username)
        
        if not user:
            logger.info(f"Failed login attempt - user not found: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        if not verify_password(form_data.password, user.hashed_password):
            logger.info(f"Failed login attempt - incorrect password for: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Check if user is active
        if not user.is_active:
            logger.info(f"Login attempt for inactive account: {form_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Account is inactive",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Create access token
        logger.debug(f"Generating token for user: {user.username}")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "id": str(user.id), "role": user.role},
            expires_delta=access_token_expires
        )
        
        logger.info(f"Successful login for user: {user.username}")
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log unexpected errors
        error_details = traceback.format_exc()
        logger.error(f"Unexpected error during token generation: {e}\n{error_details}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred. Please try again later."
        )

@router.post("/login", response_model=Token)
async def login(request: Request, login_data: LoginRequest):
    # Log the login request
    logger.info(f"Login request for email: {login_data.email} from {request.client.host}")
    
    try:
        # Verify database connection first
        db_connected = await check_db_connection()
        if not db_connected:
            logger.error("Database connection failed during login")
            raise HTTPException(
                status_code=503,
                detail="Database service unavailable. Please try again later."
            )
        
        # Authenticate user
        logger.debug(f"Authenticating user by email: {login_data.email}")
        user = await UserQueries.get_user_by_email(login_data.email)
        
        if not user:
            logger.info(f"Failed login attempt - user not found: {login_data.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
        if not verify_password(login_data.password, user.hashed_password):
            logger.info(f"Failed login attempt - incorrect password for: {login_data.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Check if user is active
        if not user.is_active:
            logger.info(f"Login attempt for inactive account: {login_data.email}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Account is inactive",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Create access token
        logger.debug(f"Generating token for user: {user.username}")
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username, "id": str(user.id), "role": user.role},
            expires_delta=access_token_expires
        )
        
        logger.info(f"Successful login for user: {user.username}")
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Log unexpected errors
        error_details = traceback.format_exc()
        logger.error(f"Unexpected error during login: {e}\n{error_details}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred. Please try again later."
        )