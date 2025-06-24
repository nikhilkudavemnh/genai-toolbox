import logging
import os
import json
from logging.handlers import RotatingFileHandler
from .config import Settings
from datetime import datetime


log_dir = Settings.LOG_DIR if hasattr(Settings, 'LOG_DIR') else 'logs'
file_name = os.path.join(log_dir,'app.log')

os.makedirs(log_dir, exist_ok=True)


class JsonLogFormatter(logging.Formatter):

     def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "name": record.name,
            "message": record.getMessage(),
            "filename": record.filename,
            "line": record.lineno,
        }

        # Include extra fields like method, url, status_code, etc.
        for attr in ['method', 'url', 'status_code', 'process_time_ms','client_ip']:
            if hasattr(record, attr):
                log_record[attr] = getattr(record, attr)

        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_record)


def setup_logger(name: str = "app_logger") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Remove any existing handlers (safe reset)
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = JsonLogFormatter()

    file_handler = RotatingFileHandler(file_name, maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger




logger = setup_logger()