import array
def get_array_item_count(array, item):
        return array.count(item)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)