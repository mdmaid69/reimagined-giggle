import logging
def log_message(message):
        logging.info(message)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)