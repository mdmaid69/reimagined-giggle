import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_area(radius):
        return 3.14 * radius * radius