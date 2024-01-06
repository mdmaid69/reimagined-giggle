import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)