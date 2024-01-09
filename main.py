import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())