def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)