import array
def get_array_as_complex(array):
        return complex(array[0])
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))