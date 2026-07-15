from motor.motor_asyncio import AsyncIOMotorClient

from ..connect4game.settings import settings


def get_mongodb_client() -> AsyncIOMotorClient:
    "Get MongoDB client instance."
    return AsyncIOMotorClient(settings.MONGO_DB_URL)  # type: ignore[var-annotated]
