import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable