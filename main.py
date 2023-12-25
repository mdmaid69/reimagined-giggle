import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import logging
def setup_logging(level):
        logging.basicConfig(level=level)