import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import collections
def create_queue():
        return collections.deque()