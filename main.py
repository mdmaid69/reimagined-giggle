import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array