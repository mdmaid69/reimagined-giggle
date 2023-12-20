import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)