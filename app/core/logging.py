import logging
import json
from datetime import datetime
from app.core.config import settings
import contextvars

request_id_context = contextvars.ContextVar('request_id', default='N/A')

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "message": record.getMessage(),
            "request_id": request_id_context.get()
        }
        return json.dumps(log_entry)

def setup_logging():
    # Create JSON formatter
    formatter = JSONFormatter()

    # Get root logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, settings.log_level.upper(), logging.INFO))

    # Create console handler
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Suppress uvicorn logs to avoid drowning app logs
    uvicorn_logger = logging.getLogger('uvicorn')
    uvicorn_logger.setLevel(logging.WARNING)
    uvicorn_access_logger = logging.getLogger('uvicorn.access')
    uvicorn_access_logger.setLevel(logging.WARNING)
