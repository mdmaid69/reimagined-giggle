def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))