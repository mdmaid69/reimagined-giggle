import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")