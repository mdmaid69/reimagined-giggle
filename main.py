import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))