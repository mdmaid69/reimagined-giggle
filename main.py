import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import logging
def setup_logging(level):
        logging.basicConfig(level=level)