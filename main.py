import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def extend_array(array, iterable):
        array.extend(iterable)