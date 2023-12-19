import time
def get_current_time():
        return time.ctime()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)