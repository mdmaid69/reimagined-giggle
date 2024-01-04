import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)