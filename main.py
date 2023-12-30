import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)