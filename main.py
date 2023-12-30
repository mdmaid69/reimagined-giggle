import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")