import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def get_array_as_frozenset(array):
        return frozenset(array)