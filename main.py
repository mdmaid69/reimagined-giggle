import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a