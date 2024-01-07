import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))