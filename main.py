import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def get_array_index(array, item):
        return array.index(item)