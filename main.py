import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")