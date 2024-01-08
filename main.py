import time
def get_time_since_epoch():
        return time.time()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)