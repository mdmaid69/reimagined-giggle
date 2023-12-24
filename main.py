import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))