import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)