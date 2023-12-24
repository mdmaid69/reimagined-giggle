import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import logging
def log_message(message):
        logging.info(message)