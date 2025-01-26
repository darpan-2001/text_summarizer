import os
import sys
import logging
from pathlib import Path



log_dir = Path(f"logs")
log_dir.mkdir(parents=True, exist_ok=True)  # Ensure the log directory exists

# log file path
log_filepath = log_dir / "application.log"


log_format = "[%(asctime)s]: %(levelname)s - %(message)s"
logging.basicConfig(
    level=logging.INFO, 
    format=log_format,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout),            
    ]
)


logger = logging.getLogger("text_summarizer_logger")

# logger.info("Logger initialized successfully.")