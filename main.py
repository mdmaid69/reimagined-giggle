import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")