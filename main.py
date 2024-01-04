import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a