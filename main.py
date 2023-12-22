import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import collections
def create_priority_queue():
        return collections.deque()