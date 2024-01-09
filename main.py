n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))