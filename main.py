import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)