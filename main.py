import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)