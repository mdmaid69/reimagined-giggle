def find_difference(list1, list2):
        return set(list1) - set(list2)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)