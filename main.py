import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)