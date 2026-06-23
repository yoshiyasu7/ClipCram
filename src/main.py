from contextlib import asynccontextmanager
import uuid
import structlog
import uvicorn
from fastapi import FastAPI, Request

from src.api.v1.router import api_v1_router

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(_app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(api_v1_router)


@app.middleware("http")
async def add_request_id_logging(request: Request, call_next):
    request_id = str(uuid.uuid4())
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(request_id=request_id)
    logger.info("API request started", request=request, request_id=request_id)

    response = await call_next(request)

    logger.info("API request finished", response=response, request_id=request_id)
    return response


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )