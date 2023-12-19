import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a