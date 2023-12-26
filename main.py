import logging
def log_message(message):
        logging.info(message)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)