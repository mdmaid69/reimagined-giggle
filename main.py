import logging
def log_message(message):
        logging.info(message)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)