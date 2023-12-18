import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def convert_array_to_string(array):
        return array.tostring()