import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def find_union(list1, list2):
        return set(list1) | set(list2)