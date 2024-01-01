import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import array
def get_array_as_frozenset(array):
        return frozenset(array)