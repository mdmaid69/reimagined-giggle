import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def iterate_over_array(array):
        for item in array:
        print(item)