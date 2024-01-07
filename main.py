import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)