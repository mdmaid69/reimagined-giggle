import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)