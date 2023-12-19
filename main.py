import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))