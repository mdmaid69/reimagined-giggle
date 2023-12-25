import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))