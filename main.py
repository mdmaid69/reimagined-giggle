import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)