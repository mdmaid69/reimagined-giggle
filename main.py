import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")