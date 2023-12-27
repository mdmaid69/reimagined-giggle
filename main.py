import time
print(time.time())
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h