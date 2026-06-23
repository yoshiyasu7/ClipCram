from fastapi import APIRouter

from src.api.v1.endpoints import router as compress_router


api_v1_router = APIRouter(prefix="/v1")

api_v1_router.include_router(compress_router)