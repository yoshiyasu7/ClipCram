from fastapi import APIRouter
from fastapi import UploadFile, File
import structlog

# from src.workers.tasks import compress_video_task

logger = structlog.get_logger()


router = APIRouter(prefix="/compress")


@router.post("/video")
async def compress_video(video: UploadFile = File(...)):
    ctx = structlog.contextvars.get_contextvars()
    req_id = ctx.get("request_id")
    logger.info("Received compression request, dispatching to Celery")

    # compress_video_task.delay(video.file, req_id)

    return {"status": "accepted", "request_id": req_id}