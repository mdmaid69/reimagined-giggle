import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def clear_array(array):
        array *= 0