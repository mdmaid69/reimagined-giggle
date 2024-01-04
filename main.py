import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import logging
def log_message(message):
        logging.info(message)