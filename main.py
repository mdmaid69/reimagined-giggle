import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))