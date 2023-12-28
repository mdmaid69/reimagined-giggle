import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))