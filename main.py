n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)