from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI

from .db.utils import get_mongodb_client
from .api.views import router as api_router
from .connect4game.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # set up MongoDB
    client = get_mongodb_client()
    db = client.get_database(settings.MONGO_DB_DB)
    app.mongodb = db  # type: ignore[attr-defined]
    yield
    # close MongoDB connection
    client.close()  # type: ignore[attr-defined, operator]


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "Connect4 Game World!"}
