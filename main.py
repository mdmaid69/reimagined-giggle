import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
def is_odd(n):
        return n % 2 != 0