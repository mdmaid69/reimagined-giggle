import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))