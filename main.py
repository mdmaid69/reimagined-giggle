import logging
def log_message(message):
        logging.info(message)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))