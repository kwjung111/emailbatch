import logging
import os
from logging.handlers import RotatingFileHandler
from config import LOG_DIR

LOG_FILE = "batch.log"
os.makedirs(LOG_DIR, exist_ok=True)

def get_logger(name=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # 중복 핸들러 방지
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s - %(message)s")

        # 파일 핸들러 (최대 5MB, 3개 유지)
        file_handler = RotatingFileHandler(
            os.path.join(LOG_DIR, LOG_FILE),
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # 콘솔 핸들러
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger