import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")