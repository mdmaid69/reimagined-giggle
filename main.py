import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))