import time
def get_current_time():
        return time.ctime()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)