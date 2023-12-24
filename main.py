import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)