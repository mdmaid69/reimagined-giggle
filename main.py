import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))