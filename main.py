import array
def get_string_from_array(array):
        return array.tobytes()
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))