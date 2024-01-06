import collections
def create_counter():
        return collections.Counter()
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)