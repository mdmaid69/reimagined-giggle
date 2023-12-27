import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a