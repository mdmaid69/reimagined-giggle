import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import logging
def setup_logging(level):
        logging.basicConfig(level=level)