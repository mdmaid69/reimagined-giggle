import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))