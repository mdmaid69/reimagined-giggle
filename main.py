import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import time
def get_current_time():
        return time.time()