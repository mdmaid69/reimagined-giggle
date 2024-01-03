import time
def get_time_since_epoch():
        return time.time()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)