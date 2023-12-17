import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)