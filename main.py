import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())