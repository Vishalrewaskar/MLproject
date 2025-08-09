import logging
import os
from datetime import datetime

# Create a log file -> Based on Current date and time
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  

# Create path to store log file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # ( current working directory/logs/08_06_2025_12_30_00.log ) 
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)