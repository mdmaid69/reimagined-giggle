import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import logging
def setup_logging(level):
        logging.basicConfig(level=level)