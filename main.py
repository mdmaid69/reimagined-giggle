import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def insert_into_array(array, i, item):
        array.insert(i, item)