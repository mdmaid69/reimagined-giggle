import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")