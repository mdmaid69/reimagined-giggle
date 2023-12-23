import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)