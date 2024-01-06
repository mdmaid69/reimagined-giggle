import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)