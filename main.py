import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)