import time
def get_current_time():
        return time.time()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)