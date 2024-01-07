import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)