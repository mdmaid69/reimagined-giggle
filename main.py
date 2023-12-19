import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)