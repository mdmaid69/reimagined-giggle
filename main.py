import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def extend_array(array, iterable):
        array.extend(iterable)