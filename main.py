import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)