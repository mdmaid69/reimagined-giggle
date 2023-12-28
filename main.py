import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import time
def get_current_time():
        return time.ctime()