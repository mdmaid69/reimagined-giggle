import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)