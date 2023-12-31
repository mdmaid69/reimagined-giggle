import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)