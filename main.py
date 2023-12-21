import array
def get_array_slice(array, i, j):
        return array[i:j]
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))