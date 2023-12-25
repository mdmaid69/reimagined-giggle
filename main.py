import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)