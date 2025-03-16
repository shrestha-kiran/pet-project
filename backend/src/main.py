from contextlib import asynccontextmanager

from fastapi import FastAPI

from .api.views import router as api_router
from .db.utils import get_mongodb


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    mongodb = get_mongodb()
    app.mongodb = mongodb
    yield
    # Shutdown code
    app.mongodb.close()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "pet project world"}
