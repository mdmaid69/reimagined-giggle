import array
def get_array_as_list(array):
        return list(array)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))