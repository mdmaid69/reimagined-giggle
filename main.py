import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import logging
def setup_logging(level):
        logging.basicConfig(level=level)