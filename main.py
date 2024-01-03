import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def append_to_array(array, item):
        array.append(item)