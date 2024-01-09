import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import time
def get_time_since_epoch():
        return time.time()