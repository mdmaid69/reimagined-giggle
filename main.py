import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))