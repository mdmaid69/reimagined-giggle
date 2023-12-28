n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)