import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import logging
def log_message(message):
        logging.info(message)