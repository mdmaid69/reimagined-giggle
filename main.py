import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def convert_array_to_bytes(array):
        return array.tobytes()