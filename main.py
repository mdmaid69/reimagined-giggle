import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def get_array_slice(array, i, j):
        return array[i:j]