import collections
def create_counter():
        return collections.Counter()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h