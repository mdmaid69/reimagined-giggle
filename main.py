import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)