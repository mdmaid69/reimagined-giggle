def find_difference(list1, list2):
        return set(list1) - set(list2)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)