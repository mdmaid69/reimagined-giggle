import logging
def log_message(message):
        logging.info(message)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)