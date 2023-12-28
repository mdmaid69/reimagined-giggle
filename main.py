import array
def get_array_typecode(array):
        return array.typecode
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))