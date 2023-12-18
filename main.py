import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))