import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import numpy as np
print(np.array([1, 2, 3]))