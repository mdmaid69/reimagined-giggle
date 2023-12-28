import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)