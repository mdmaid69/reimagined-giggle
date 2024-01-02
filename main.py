import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))