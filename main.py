import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)