import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import collections
def create_stack():
        return collections.deque()