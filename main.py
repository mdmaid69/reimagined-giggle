import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")