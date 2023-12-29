import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))