import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)