import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def get_array_as_bytearray(array):
        return bytearray(array)