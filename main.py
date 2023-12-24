import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)