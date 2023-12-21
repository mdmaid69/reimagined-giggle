import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}