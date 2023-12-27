import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
def is_odd(n):
        return n % 2 != 0