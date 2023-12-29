import logging
def log_message(message):
        logging.info(message)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)