import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)