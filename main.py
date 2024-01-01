import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)