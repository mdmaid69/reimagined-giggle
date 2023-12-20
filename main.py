import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def get_array_itemsize(array):
        return array.itemsize