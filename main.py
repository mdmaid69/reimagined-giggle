import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)