import array
def get_array_as_list(array):
        return list(array)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))