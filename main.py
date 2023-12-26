import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)