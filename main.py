import re
def split_string(pattern, string):
        return re.split(pattern, string)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)