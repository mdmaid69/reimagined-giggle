import logging
def setup_logging(level):
        logging.basicConfig(level=level)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)