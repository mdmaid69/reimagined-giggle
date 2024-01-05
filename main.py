import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)