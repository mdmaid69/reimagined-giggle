import datetime
def get_current_datetime():
        return datetime.datetime.now()
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)