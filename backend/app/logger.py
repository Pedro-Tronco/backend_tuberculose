import logging
from logging.handlers import RotatingFileHandler
from os import path

def setup_logging() -> logging.Logger:
    logger = logging.getLogger("AppLogger")
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "[%(asctime)s - %(name)s] - %(levelname)s - %(message)s"
    )


    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)

    current_dir = path.dirname(path.abspath(__file__))
    logs_dir = path.join(current_dir, "..", "logs")
    log_file_path = path.join(logs_dir, "app.log")

    fh = RotatingFileHandler(log_file_path, maxBytes=5*1024*1024, backupCount=2)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)
    
    return logger

logger = setup_logging()