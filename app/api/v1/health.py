from fastapi import APIRouter
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
def read_root():
    logger.info("Health check endpoint called")
    return {
        "status": "ok"
    }
