def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import collections
def create_counter():
        return collections.Counter()