import logging
import os
from datetime import datetime

# --- Step 1: Generate a unique log file name for this run ---
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# --- Step 2: Build the full directory path for the logs folder ---
# os.getcwd() returns the project root. We place logs/ there.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# --- Step 3: Create the logs/ directory if it doesn't exist ---
# exist_ok=True means: don't raise an error if the folder is already there
os.makedirs(logs_path, exist_ok=True)

# --- Step 4: Build the full path to the actual .log file ---
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# --- Step 5: Configure the root logger ---
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)