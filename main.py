import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def get_array_buffer_info(array):
        return array.buffer_info()