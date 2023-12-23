import array
def get_array_item_count(array, item):
        return array.count(item)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))