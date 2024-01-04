import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)