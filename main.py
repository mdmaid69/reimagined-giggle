import array
def get_array_as_repr(array):
        return repr(array)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))