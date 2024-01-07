import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")