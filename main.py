import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def get_array_as_complex(array):
        return complex(array[0])