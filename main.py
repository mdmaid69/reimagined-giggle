import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_pressure(force, area):
        return force / area