import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))