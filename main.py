import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a