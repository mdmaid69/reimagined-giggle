import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def get_array_buffer_info(array):
        return array.buffer_info()