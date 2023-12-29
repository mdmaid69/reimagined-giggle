import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)