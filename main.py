import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)