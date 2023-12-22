n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)