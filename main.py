import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import logging
def log_message(message):
        logging.info(message)