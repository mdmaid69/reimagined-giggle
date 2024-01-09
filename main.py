import logging
def log_message(message):
        logging.info(message)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)