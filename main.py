n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h