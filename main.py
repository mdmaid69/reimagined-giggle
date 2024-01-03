import array
def set_array_item(array, i, item):
        array[i] = item
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))