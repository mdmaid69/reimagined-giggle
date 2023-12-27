import logging
def log_message(message):
        logging.info(message)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)