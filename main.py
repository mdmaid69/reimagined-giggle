n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))