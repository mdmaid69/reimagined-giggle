import logging
def log_message(message):
        logging.info(message)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")