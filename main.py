n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))