import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def convert_array_to_list(array):
        return array.tolist()