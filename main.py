import array
def get_list_from_array(array):
        return array.tolist()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))