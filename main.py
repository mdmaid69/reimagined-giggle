import array
def get_array_as_memoryview(array):
        return memoryview(array)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)