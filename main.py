import logging
def log_message(message):
        logging.info(message)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)