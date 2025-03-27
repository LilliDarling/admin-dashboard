from typing import Optional
from datetime import datetime
from loguru import logger
import traceback

from models.user import User, UserRequest, UserResponse
from utils.database import engine
from utils.exceptions import handle_pymongo_error

class UserQueries:
    @staticmethod
    async def create_user(user: UserRequest) -> User:
        """
        Create a new user in the database
        """
        try:
            # Check if user already exists by email
            existing_email = await engine.find_one(User, User.email == user.email)
            if existing_email:
                logger.info(f"Registration attempt with existing email: {user.email}")
                return None
            
            # Check if username is taken
            existing_username = await engine.find_one(User, User.username == user.username)
            if existing_username:
                logger.info(f"Registration attempt with existing username: {user.username}")
                return None
            
            user_model = User(
                username=user.username,
                name=user.name,
                email=user.email,
                password=user.password
            )
            
            # Save user to database
            await engine.save(user_model)
            logger.info(f"New user created: {user.username} ({user.email})")
            return user_model
            
        except Exception as e:
            error_details = traceback.format_exc()
            logger.error(f"Error creating user: {e}\n{error_details}")
            await handle_pymongo_error(e)
            return None
    
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        """
        Get a user by email
        """
        try:
            user = await engine.find_one(User, User.email == email)
            return user
        except Exception as e:
            error_details = traceback.format_exc()
            logger.error(f"Error getting user by email: {e}\n{error_details}")
            await handle_pymongo_error(e)
            return None
    
    @staticmethod
    async def get_user_by_username(username: str) -> Optional[User]:
        """
        Get a user by username
        """
        try:
            user = await engine.find_one(User, User.username == username)
            return user
        except Exception as e:
            error_details = traceback.format_exc()
            logger.error(f"Error getting user by username: {e}\n{error_details}")
            await handle_pymongo_error(e)
            return None