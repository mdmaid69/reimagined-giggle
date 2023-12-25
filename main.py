import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)