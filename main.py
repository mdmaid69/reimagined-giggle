import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import logging
def setup_logging(level):
        logging.basicConfig(level=level)