import sys
print(sys.version)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h