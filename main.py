import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def get_bytes_from_array(array):
        return array.tobytes()