import logging
import os
from datetime import datetime

# Create the logs directory if it doesn't exist
logs_dir = os.path.join(os.getcwd(), "logs")
print(f"Creating logs directory at: {logs_dir}")  # Debug print
os.makedirs(logs_dir, exist_ok=True)

# Define the log file name and path
log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_file_path = os.path.join(logs_dir, log_file)
print(f"Log file will be created at: {log_file_path}")  # Debug print

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

