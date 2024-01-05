import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)