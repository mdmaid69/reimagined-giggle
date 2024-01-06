import sys
print(sys.version)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)