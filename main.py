import logging
def log_message(message):
        logging.info(message)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)