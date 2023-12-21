import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)