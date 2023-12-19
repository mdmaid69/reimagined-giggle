n = 10
print("Square numbers:", [x**2 for x in range(n)])
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)