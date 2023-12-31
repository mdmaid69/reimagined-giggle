import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)