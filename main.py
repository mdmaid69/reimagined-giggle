import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_area_circle(r):
        return 3.14 * r**2