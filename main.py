import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))