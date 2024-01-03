import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)