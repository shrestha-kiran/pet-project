from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from ..pet_project.settings import settings


def get_mongodb() -> AsyncIOMotorDatabase:
    client = AsyncIOMotorClient(settings.MONGO_DB_URL)
    return client[settings.MONGO_DB_DB]
