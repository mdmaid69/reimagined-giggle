import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def check_if_array_contains_item(array, item):
        return item in array