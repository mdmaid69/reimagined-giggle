import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import collections
def create_counter():
        return collections.Counter()