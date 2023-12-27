import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)