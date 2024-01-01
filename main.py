import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import datetime
def get_current_datetime():
        return datetime.datetime.now()