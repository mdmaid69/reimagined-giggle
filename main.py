import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)