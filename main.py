import array
def get_array_as_frozenset(array):
        return frozenset(array)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)