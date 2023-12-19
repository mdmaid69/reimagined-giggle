import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def check_if_array_contains_item(array, item):
        return item in array