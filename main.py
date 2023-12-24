import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)