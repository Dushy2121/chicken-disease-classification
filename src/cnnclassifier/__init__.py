import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s: %(module)s: - %(message)s]"

log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    #handlers is used to specify the output of the logs
    #here we are specifying two handlers, one for file and one for console output
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("cnn_classifier1")
logger.info("Logging has been set up successfully.")