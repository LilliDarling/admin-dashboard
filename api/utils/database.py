from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
from loguru import logger
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger.info(f"Using MongoDB Atlas connection")

client = AsyncIOMotorClient(os.environ["MONGODB_ATLAS_URL"])
engine = AIOEngine(client=client, database='dashboard')


async def initialize_database():
    """
    Initialize the database connection and configure models
    """
    try:
        await client.admin.command('ping')
        logger.info("MongoDB connection successful")

        from models.post import Post
        from models.quote import Quote
        from models.user import User

        await engine.configure_database([Post, Quote, User])
        logger.info("Database models configured successfully")

    except Exception as e:
        logger.error(f"Database initialization error: {e}")
        raise
