import array
def get_array_as_bytes(array):
        return bytes(array)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)