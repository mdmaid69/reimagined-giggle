import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def remove_duplicates(lst):
        return list(set(lst))