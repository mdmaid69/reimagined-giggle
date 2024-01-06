import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))