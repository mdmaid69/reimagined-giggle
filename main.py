import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a