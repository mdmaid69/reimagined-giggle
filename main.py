import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)