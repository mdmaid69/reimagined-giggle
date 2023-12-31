n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)