import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)