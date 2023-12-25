import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)