import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a