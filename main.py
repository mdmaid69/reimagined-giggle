import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)