import logging
import os
import sys
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = 'logs'
os.makedirs(logs_dir, exist_ok=True)

log_filepath = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("TextSummarizerLogger")