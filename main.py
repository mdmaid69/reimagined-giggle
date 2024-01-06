import array
def get_array_as_bytearray(array):
        return bytearray(array)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))