import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")