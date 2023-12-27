import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)