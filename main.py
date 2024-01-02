import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def convert_bytes_to_array(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a