import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)