import array
def get_array_as_set(array):
        return set(array)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))