import time
print(time.time())
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)