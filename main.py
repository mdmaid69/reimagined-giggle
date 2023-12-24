import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def find_union(list1, list2):
        return set(list1) | set(list2)