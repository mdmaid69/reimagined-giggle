import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)