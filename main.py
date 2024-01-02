import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)