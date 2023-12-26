import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")