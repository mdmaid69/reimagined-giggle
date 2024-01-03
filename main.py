import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)