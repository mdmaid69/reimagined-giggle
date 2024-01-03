import time
def get_time_since_epoch():
        return time.time()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)