import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array