import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}