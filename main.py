import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)