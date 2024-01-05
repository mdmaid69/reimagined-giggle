import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)