import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())