import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)