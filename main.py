import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def remove_from_array(array, item):
        array.remove(item)