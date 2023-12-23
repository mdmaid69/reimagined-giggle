import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))