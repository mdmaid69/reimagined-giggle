n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)