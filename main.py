n = 10
print("Square numbers:", [x**2 for x in range(n)])
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)