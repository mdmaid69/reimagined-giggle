import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)