import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)