n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))