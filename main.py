import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))