import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)