import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)