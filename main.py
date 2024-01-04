import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import sys
print(sys.version)