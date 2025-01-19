import logging
from datetime import datetime

def setup_logger(name: str, log_file: str, level=logging.INFO):
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s [%(name)s] %(message)s'
    )
    
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger

# 로거 생성
logger = setup_logger('book_management', 'app.log')
