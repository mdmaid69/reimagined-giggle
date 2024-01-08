import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)