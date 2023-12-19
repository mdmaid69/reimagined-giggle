import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def get_array_from_string(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a