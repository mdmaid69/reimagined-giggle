import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)