import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def extend_array(array, iterable):
        array.extend(iterable)