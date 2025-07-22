import logging
import logging.handlers
import json

def get_logger(name="MyAppLogger", log_file="splunk_log.json"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        handler = logging.FileHandler(log_file)
        handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
