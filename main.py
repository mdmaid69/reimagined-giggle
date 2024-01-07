import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def get_string_from_array(array):
        return array.tobytes()