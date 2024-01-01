import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))