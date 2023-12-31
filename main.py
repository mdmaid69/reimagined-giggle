import re
def split_string(pattern, string):
        return re.split(pattern, string)
import logging
def log_message(message):
        logging.info(message)