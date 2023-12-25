import logging
def log_message(message):
        logging.info(message)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)