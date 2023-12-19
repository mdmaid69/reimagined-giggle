import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)