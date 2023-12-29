import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h