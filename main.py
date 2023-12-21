import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a