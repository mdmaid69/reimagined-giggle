import datetime
def get_current_datetime():
        return datetime.datetime.now()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)