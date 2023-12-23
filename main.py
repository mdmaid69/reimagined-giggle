import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))