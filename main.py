def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)