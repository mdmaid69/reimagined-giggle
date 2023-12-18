import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)