import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)