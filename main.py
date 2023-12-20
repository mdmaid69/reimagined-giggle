import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)