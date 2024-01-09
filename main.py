import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))