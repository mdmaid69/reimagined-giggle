import collections
def create_queue():
        return collections.deque()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h