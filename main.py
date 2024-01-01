import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))