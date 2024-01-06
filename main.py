import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")