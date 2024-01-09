import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)