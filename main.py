import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)