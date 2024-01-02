from collections import Counter
print(Counter("hello world"))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h