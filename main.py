n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)