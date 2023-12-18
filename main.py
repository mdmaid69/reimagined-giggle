import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)