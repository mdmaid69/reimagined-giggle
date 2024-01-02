import os
print(os.getcwd())
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h