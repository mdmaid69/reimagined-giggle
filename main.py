n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)