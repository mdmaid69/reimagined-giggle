import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import datetime
def get_current_datetime():
        return datetime.datetime.now()