import collections
def create_stack():
        return collections.deque()
import logging
def setup_logging(level):
        logging.basicConfig(level=level)