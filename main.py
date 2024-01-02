import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import collections
def count_elements(iterable):
        return collections.Counter(iterable)