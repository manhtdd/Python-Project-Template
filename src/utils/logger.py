from icecream import ic as logger
from datetime import datetime
import os

# Create a folder named 'logs' if it doesn't exist
if not os.path.exists(f"{os.getcwd()}/logs"):
    os.makedirs(f"{os.getcwd()}/logs")

# Define a file to log IceCream output
log_file_path = os.path.join(f"{os.getcwd()}/logs", "app.log")

# Replace logging configuration with IceCream configuration
logger.configureOutput(
    prefix=f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | ',
    outputFunction=lambda x: open(log_file_path, "a").write(x + "\n"),
)

logger.configureOutput(prefix=f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | ')