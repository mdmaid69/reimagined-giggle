import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))