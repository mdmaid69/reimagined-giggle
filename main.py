import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))