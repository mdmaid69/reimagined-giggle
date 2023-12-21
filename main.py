def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))