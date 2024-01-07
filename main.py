import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)