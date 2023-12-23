import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import re
def split_string(pattern, string):
        return re.split(pattern, string)