import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h